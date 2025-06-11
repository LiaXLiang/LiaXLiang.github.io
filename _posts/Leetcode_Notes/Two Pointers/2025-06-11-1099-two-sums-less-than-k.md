---
title: 1099 Two Sum Less Than K
date: 2025-06-101
categories: [Leetcode_Notes, Two Pointers]
---
### Solution
```java
class Solution {
    public int twoSumLessThanK(int[] nums, int k) {
        quickSort(nums, 0, nums.length - 1);

        int left = 0;
        int right = nums.length - 1;
        int maxSum = -1;

        while (left < right) {
            int sum = nums[left] + nums[right];
            if (sum >= k) {
                right--;
            } else {
                maxSum = Math.max(maxSum, sum);
                left++;
            }
        }

        return maxSum;
    }

    private void quickSort(int[] nums, int left, int right) {
        if (left >= right) return;

        int pivotIndex = partition(nums, left, right);
        quickSort(nums, left, pivotIndex - 1);
        quickSort(nums, pivotIndex + 1, right);
    }

    private int partition(int[] nums, int left, int right) {
        int pivot = nums[right];
        int i = left;
        int j = right - 1;

        while (i <= j) {
            while (i <= j && nums[i] < pivot) i++;
            while (i <= j && nums[j] >= pivot) j--;

            if (i < j) {
                swap(nums, i, j);
            }
        }

        swap(nums, i, right);  // put pivot in correct position
        return i;
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```
```
Time Complexity: O(NlogN)
Space Complexity: O(logN)
Quick Sort is an in-place sorting algorithm, it incurs additional space overhead on the call stack due to its recursive nature, which can reach up to O(n) in the worst case and O(log n) on average, depending on the partitioning quality.
```