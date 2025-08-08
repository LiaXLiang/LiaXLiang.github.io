---
title: 45. Jump Game II
date: 2025-08-08
categories: [Leetcode_Notes, Dynamic Programming]
---

## Core Idea
This problem is a typical application of the greedy algorithm. The key idea is to always make the locally optimal choice at each step, which in this case means jumping to the position that maximizes our future reach.

## Explanation with Example:
Consider the array [2, 3, 3, 2, 0, 4].

1. Initial Position:
    
    We start from the first element,` nums[0] = 2`. This means that from position 0, we can jump either to position 1 or position 2. These two positions are reachable.

2. Greedy Choice:
    Now, we need to decide which position will allow us to jump the farthest in the next round. This is done by comparing the possible jumps:
    - From position 0 (nums[0] = 2), we can jump to position 1 or 2.
    - From position 1 (nums[1] = 3), we can jump to position 2, 3, or 4.
    - From position 2 (nums[2] = 3), we can jump to position 3, 4, or 5.

    To decide which position to move to, we calculate the farthest reachable position at each step by comparing `curPos + nums[curPos]` for each possible jump.

3. Updating the Current Position:
    At each step, we update `curPos` to the position that gives us the farthest possible reach in the next round. This is done by selecting the position with the largest value of `i + nums[i]` in the current jump range.

4. Termination Condition:

    The process continues until we reach the last element in the array. If at any point, `curPos + nums[curPos]` reaches or exceeds the end of the array, we can terminate the process and return the number of jumps.

### Solution
```java
class Solution {
    public int jump(int[] nums) {
        int curPos = 0; // Current position 
        int res = 0; // Count of jumps made so far
        int n = nums.length; 
        
        while (curPos < n - 1) { // Continue while we're not at the last element
            // If the current jump can directly reach or exceed the last element
            if (curPos + nums[curPos] >= n - 1) return res + 1;
            
            // Find the farthest position we can jump to within the current range
            int next = curPos; 
            for (int i = curPos + 1; i <= curPos + nums[curPos]; i++) {
                // Update next if we find a position that can reach further
                if (i + nums[i] > next + nums[next]) {
                    next = i;
                }
            }
            
            // Jump to the farthest reachable position
            curPos = next;
            res++; // Increment the jump count
        }
        
        return res; 
    }
}
```

```
Time Complexity: O(N)
Space Complexity: O(1)
```