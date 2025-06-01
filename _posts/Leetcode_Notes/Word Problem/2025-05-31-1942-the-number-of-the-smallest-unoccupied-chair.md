---
title: 1942 The Number of the Smallest Unoccupied Chair
date: 2025-05-31
categories: [Leetcode_Notes, Word Problem]
---

### Problem Analogy: Friends at a Movie Theater
Imagine we're working at a movie theater with an unlimited supply of seats.

We're expecting *n* friends, each arriving and leaving at different times. Some stay briefly, others stay longer, and some friends arrive or leave at the same time.

Our task is to simulate seat assignment with the following rules:
- Assign each arriving friend the **smallest-numbered available** seat.
- When someone leaves, **free up their seat** for future use. 
  - If a friend arrives and another leaves at the same time, handle departures first — this frees up seats for the new arrivals.
- Determine **which seat our best friend (with ID ```targetFriend``` will end up sitting in**)
  
### Event-Based Priority Queue Simulation
#### Core Idea
This approach simulates the system by **processing events in chronological order**. Each friend generates two events: an *arrival* and a *departure*.

#### Key Data Structures:
- Available seats (Min-Heap)
  - It automatically gives us the **smallest-numbered available seat** whenever needed.
- Sorted arrival events (Arrays)
  - We separately track all **arrival events** and **leave events** in two Arrays, both sorted by time
    - ```arrivals[][]```: an **int[][]** array storing [arrival_time, friend_id], sorted by arrival time.
    - ```leaves[][]```: an **int[][]** array storing [leave_time, friend_id], sorted by leave time.
- Seat assignment record (HashMap)
  - Track which friend is sitting in which seat.
  - When someone leaves, use this to know which seat to return to the pool.
  
### 📌 Algorithm
- (1) Initialize the min-heap with all seat numbers: 0 to n-1.
- (2) - Create two arrays `arrivals[][]` and `leaves[][]`, each storing `[time, friend_id]`.
   - Sort both arrays by time (ascending).
- (3) **Simulate each arrival** in order:
   - Before handling the current arrival, **process all friends who have already left** (i.e., whose leave time ≤ current time):
     - For each such friend:
       - Look up their seat in the hashmap.
       - Return the seat to the min-heap.
   - Assign the arriving friend the **smallest-numbered available seat** (pop from heap).
   - Update the hashmap to record the seat assignment.
   - If the arriving friend is `targetFriend`, **return the assigned seat** immediately.
  
### Solution
```java
class Solution {
    public int smallestChair(int[][] times, int targetFriend) {
        int numFriends= times.length;

        //Step 1: Initialize a min-heap to manage available chairs
        PriorityQueue<Integer> availableChairs = new PriorityQueue<>();
        for(int i = 0; i < numFriends; i++){
            availableChairs.offer(i);
        }

        //Step2.1: Extract and tag all arrival and leave events
        int[][] arrivals = new int[numFriends][2]; 
        int[][] leaves = new int[numFriends][2];  

        for(int i = 0; i < numFriends; i++){
            arrivals[i][0] = times[i][0];
            arrivals[i][1] = i;
            leaves[i][0] = times[i][1];
            leaves[i][1] = i;
        }

        // Step 2.2: Sort events by time
        Arrays.sort(arrivals, Comparator.comparingInt(a -> a[0]));
        Arrays.sort(leaves, Comparator.comparingInt(a -> a[0]));


        // Step3: Map to record each friend's current chair assignment
        HashMap<Integer, Integer> chairAssignment = new HashMap<>();

        // Step4: Start simulating
        int leaveIndex = 0; // Pointer for leave events
        for(int[] arr: arrivals){
            int arrivalTime = arr[0];
            int arrivingPerson = arr[1];


            // Handle all leave events that happen before or at this arrival time
            while(leaveIndex < numFriends && leaves[leaveIndex][0] <= arrivalTime){
                int leavingPerson = leaves[leaveIndex][1];
                int freedChair = chairAssignment.get(leavingPerson);
                availableChairs.offer(freedChair);
                chairAssignment.remove(leavingPerson);
                leaveIndex++;

            }

            // Assign the smallest available chair to the arriving friend
            int assignedChairId = availableChairs.poll();
            chairAssignment.put(arrivingPerson, assignedChairId);
            if(arrivingPerson == targetFriend) return assignedChairId;
        }

        // According to the problem constraints, this line is never reached
        return -1; 
    }
}
```
```
Time Complexity: O(NlogN)

Let N be the number of friends:
- Initialization of the heap with n chairs: 
    · O(N);
- Constructing arrival and leave event arrays,
    · i.e., a single pass through the times-array: O(N);
- Sorting the arrival and leave arrays: 
    · O(NlogN) for each 
    -> O(NlogN);
- Main simulation loop over arrivals: 
    · <i> We iterate through n arrivals. 
    · <ii> For each arrival, we may process multiple departures. 
    · <iii> Each heap operation (poll or offer) takes O(logN).
    · <iv> Since each friend arrives and leaves once, we perform at most: 
        n heap insertions + n heap removals
    · the total heap constuction operation cost is O(NlogN)
- Total Time Complexity: O(NlogN)

Space Complexity: O(N)

- Heap 'availableChairs' stores at most n chair IDs 
    - O(N);
- Event arrays arrivals and leaves each of size n
    - O(N);
- Chair assignment map stores up to n entries (friend → chair)
    - O(N)
- Total Space Complexity: O(N)
