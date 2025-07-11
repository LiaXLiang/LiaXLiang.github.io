---
title: 33. Search in Rotated Sorted Array
date: 2025-07-11
categories: [Leetcode_Notes, Binary Search]
---

## Core Idea
A subarray `nums[left ... right]` is ordered if and only if `nums[left] <= nums[right]`. Otherwise, it must contain the rotation pivot and thus be disordered.

This leads to a modified binary search approach. At each iteration:

- We divide the array into two halves.
- At least ONE half is always sorted. We check whether the target lies within the sorted half.
  - If it does, we perform binary search within that half.
  - Otherwise, we recursively search in the disordered half (which, again, contains ONE sorted and ONE unsorted segment).


##  Key Difference from Ordinary Binary Search
In **classical** binary search, **the entire array is sorted**, and decisions are based solely on the comparison between `target` and `nums[mid]`.

In the rotated array variant, our binary search relies on evaluating which half is sorted and using this property to guide the direction of the search:

- If the left half is sorted: check if the target lies in `[nums[left] ... nums[mid]]`

- If the right half is sorted: check if the target lies in` [nums[mid] ... nums[right]]`

This introduces a layer of segment-wise logic that does not exist in standard binary search.


### Solution
```java
class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            // Compute mid without overflow
            int mid = left + (right - left) / 2;

            // Found target
            if (nums[mid] == target) {
                return mid;
            }

            // Left half is sorted
            if (nums[left] <= nums[mid]) {
                // Target is in the sorted left half
                if (target >= nums[left] && target < nums[mid]) {
                    right = mid - 1;
                } else { // Target is in the right half
                    left = mid + 1;
                }
            } 
            // Right half is sorted
            else {
                // Target is in the sorted right half
                if (target > nums[mid] && target <= nums[right]) {
                    left = mid + 1;
                } else { // Target is in the left half
                    right = mid - 1;
                }
            }
        }

        // Target not found
        return -1;
    }
}
```

```
Time Complexity: O(logN)
Space Complexity: O(1)
```