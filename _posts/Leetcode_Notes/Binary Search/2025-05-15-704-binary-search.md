---
title: 704 Binary Search
date: 2025-06-08
categories: [Leetcode_Notes, Binary Search]
---

# Binary Search
A binary search algorithm works by repeatedly dividing **the sorted array** in half until the desired element is found or until the entire array is exausted. 

Binary search involves many boundary conditions, the logic behind it is simple but rather sophisticated. For example:
- Should the loop be ```while (left < right)``` or ```while (left <= right)```?
- Should we update ```right == middle```, or ```right == midddle -1```? 
- What happens when ```left == right```?

The key to these confusions is <font color = red> the definition of the search interval </font>.



### Core Principle: Interval Definition
Binary search must preserve a strict invariant: at every iteration, the target must reside within a well-defined interval. Two standard interval definitions are:
- Left-closed, right-closed: ```[left, right]```
- Left-closed, right-open: ```[left, right)```

In each case, the loop condition, termination state, and how we update pointers must all align with the chosen definition.


Taking for example we are going to search **2** in the array ```[1, 2, 3, 4, 7, 9, 10]```.

#### I. Interval Definition: <font color = red> [left, right]</font>.
In this version, both ```left``` and ```right``` are valid candidate indices — the search space is inclusive on both ends.


   
|index:    | 0   | 1   | 2   | 3   | 4   | 5   |  6  | 
|  :--:    | :--:| :--:| :--:| :--:| :--:| :--:| :--:| 
|elements: | 1   | 2   | 3   | 4   | 7   |  9  |  10 |
|          |L = 0|      |     | M = 3    |     |     | R = 6|

  1. Invariant Maintained:
     - ```target ∈ [left, right]```
  2. Loop Condition:  
     - <font color = red> **while (left <= right)**</font>
  3. When ```left == right```:
     - the single element at that index is still valid and must be checked.
  5. Pointer Update Rules:
     - If ```nums[middle] > target```: 
       - Eliminate the right half **including middle**, search in ```[left, middle - 1]```
       - ```right = middle - 1;```
     - If ```nums[middle] < target```:
       - Eliminate the left half **including middle**, search in ```[middle + 1, right]```
       - ```left = middle + 1;```
  
| index:    | 0   | 1   | 2   |
|  :--:     | :--:| :--: | :--:|
|elements:  | 1   | 2    | 3   |
|           |L = 0| M = 1 | R = 2|


```java
class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        // Define interval as [left, right]
        int right = nums.length - 1; 

        // Since [left, right] is inclusive, use <=
        while (left <= right) { 
            // Prevents overflow
            int middle = left + (right - left) / 2; 

            if (nums[middle] == target) {
                return middle;
            } else if (nums[middle] > target) {
                // Search in [left, middle - 1]
                right = middle - 1; 
            } else {
                // Search in [middle + 1, right]
                left = middle + 1; 
            }
        }

        return -1; // Target not found
    }
}
```

#### II. Interval Definition: <font color = red> [left, right)</font>.
In this version, ```left``` is inclusive and ```right``` is exclusive. The element at index ```right``` is never considered part of the search space.

|index:    | 0   | 1   | 2   | 3   | 4   | 5   |  6  |  7  |
|  :--:    | :--:| :--:| :--:| :--:| :--:| :--:| :--:| :--:|
|elements: | 1   | 2   | 3   | 4   | 7   |  9  |  10 |     |
|          |L = 0|      |    | M = 3|    |     |      | R = 7|


  1. Invariant Maintained:
     - ```target ∈ [left, right)```
  2. Loop Condition:  
     - <font color = red> **while (left < right)**</font>
  3. When ```left == right```:
     - the loop must terminate, as this means the interval is empty.
  4. Pointer Update Rules:
     - If ```nums[middle] > target```: 
       - Eliminate the right half **including middle**, search in ```[left, middle)```
       - ```right = middle;```
       - If we **incorrectly** set ```right = middle - 1``` (as used in ```[left, right]``` intervals), we would violate the right-open invariant — it would no longer be valid to assume ```right``` is exclusive.
     - If ```nums[middle] < target```:
       - Eliminate the left half **including middle**, search in ```[middle + 1, right)```
       - ```left = middle + 1;```
       - If we **incorrectly** set ```left = middle``` — that would re-include a value already ruled out, potentially causing an infinite loop when ```left == right - 1```.


| index:    | 0   | 1   | 2   | 3    |
|  :--:     | :--:| :--: | :--:| :--:|
|elements:  | 1   | 2    | 3   |  4  |
|           |L = 0| M = 1|     | R = 3

```java
class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        // Define interval as [left, right)
        int right = nums.length; 

        // right is exclusive, so use '<'
        while (left < right) {   
            // Prevent integer overflow
            int middle = left + (right - left) / 2;

            if (nums[middle] == target) {
                return middle; 
            } else if (nums[middle] > target) {
                // Narrow to [left, middle)
                right = middle; 
            } else {
                // Narrow to [middle + 1, right)
                left = middle + 1; 
            }
        }

        return -1; // Target not found
    }
}

```



