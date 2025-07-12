---
title: 35. Search Insert Position
date: 2025-07-11
categories: [Leetcode_Notes, Binary Search]
---

## Core Idea
This is a textbook **binary search** problem. 

The goal is actually to find the **first index at which the target should be inserted** to maintain the sorted order. This is equivalent to finding the **first element that is greater than or equal to the target**.


## Why Standard Binary Search Works

This problem does **NOT** require any modification to classical binary search. We simply apply the standard algorithm and return the `left` pointer after the loop.

### Loop Mechanics

At each iteration:

We calculate the midpoint `mid = left + (right - left) / 2`
  - If `nums[mid] == target`:
    - return `mid`
  - If `nums[mid] < target`:
    -   everything up to (including) `mid` is to small
    -   the *target* must be to the right 
    -  → move `left = mid + 1`
  
  - Otherwise, the *target* is to the left
    - → move `right = mid - 1`
    
  - We stop when `left > right`.

After the loop:
  - `left` has moved past all elements **less than** the target. What remains is the exact position where the target can be inserted. This index also correctly returns the position if the target already exists.
  
  - right points to the last index where `nums[right] < target`,
  but this is not a suitable insertion point — it's one position too far left.

This is why we return *left* — it's the smallest index satisfying `nums[left] >= target`, or the length of the array if no such index exists (i.e., *target* is larger than all elements).

### Example 1: `nums = [1, 2, 3]`, `target = 1.5`

```
Initial: left = 0, right = 2
mid = 1 → nums[1] = 2 > 1.5 → move right = mid - 1 = 0

Now: left = 0, right = 0
mid = 0 → nums[0] = 1 < 1.5 → move left = mid + 1 = 1

Now: left = 1, right = 0 → loop exits
→ Return left = 1 (insert between 1 and 2)
```

### Example 2: `nums = [1, 2, 3]`, `target = 0.5`

```
Initial: left = 0, right = 2
mid = 1 → nums[1] = 2 > 0.5 → move right = mid - 1 = 0

Now: left = 0, right = 0
mid = 0 → nums[0] = 1 > 0.5 → move right = mid - 1 = -1

Now: left = 0, right = -1 → loop exits
→ Return left = 0 (insert at beginning)
```

### Solution
```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        // At the end of binary search, left is the correct insert position
        return left;
    }
}
```