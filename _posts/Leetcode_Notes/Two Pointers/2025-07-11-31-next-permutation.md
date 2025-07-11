---
title: 31. Next Permutation
date: 2025-07-11
categories: [Leetcode_Notes, Two Pointers]
---
## Core Idea
### First Observation: Look from the End
The lexicographical order of permutations is dominated by the **rightmost elements**. 

For example, a 100-element array `[1,2,3,4,....,99,100]`. 
- To generate the next permutation, it's often sufficient to examine only the last few elements.  
- In this case, simply swapping the last two numbers (`99` and `100`) yields the next permutation: `[1, 2, 3, ..., 98, 100, 99]`



This leads to a natural strategy:
- Scan the array **from right to left**, focusing on where the descending trend breaks..
  
### Second Observation: Descending Order = Maximum Permutation
If the array is in completely descending order (e.g., [9, 8, 7, 6, 5]), we have reached the maximum possible permutation. In this case, the next permutation is the minimum one:
- Simply reverse the entire array to get [5, 6, 7, 8, 9].

### Third Observation: The Pivot Point Determines the Next Step
While scanning from right to left, we look for the first pair of adjacent elements where the left element is less than the right one —  
that is, we find **the largest index `l`** such that: nums`nums[l - 1] < nums[l]`.


- The subarray to the right of *l* (`nums[l ... n-1]`) is in descending order and represents the maximum permutation for that subset.
- This pivot point *l* marks where the descending sequence (from the end) breaks.

- To generate the next permutation, we need to:
   - Identify the smallest value in `nums[l-1...n-1]` that is greater than `nums[n-1]`. Since the suffix `nums[l ... n-1]` is in descending order, this will be: `min(nums[l-1], nums[n-1])`


e.g., `nums = [x, 7, 6, 5, 3]`
- `l = 1` is the pivot point. 
- The suffix `[7, 6, 5, 3]` is in descending order. 
  
- **Case 1: `x < 3`:** (e.g., x = 2)
    - We find that `3` is the smallest number in the suffix that is larger than `x`
    - So we swap `x` and `3`: the prefix becomes `[3, ...]`
    - Then we reverse the remaining suffix: `[7, 6, 5, 2]` → `[2, 5, 6, 7]`
    - Final result: `[3, 2, 5, 6, 7]`

- **Case 2: `x ≥ 3`** (e.g., `x = 4`)
    - We find the next smallest number in the suffix greater than `x` is `5`
    - Swap `x` and `5`: prefix becomes `[5, ...]`
    - Reverse the suffix: `[7, 6, 4, 3]` → `[3, 4, 6, 7]`
    - Final result: `[5, 3, 4, 6, 7]`


### 📌 Algorithm
- (1) **Find the pivot:**  
   Scan from right to left to find the **first index `l`** such that `nums[l - 1] < nums[l]`.

- (2) If such an index exists:
    - Find the **largest index `r`** such that `nums[r] > nums[l - 1]`
    - Swap `nums[l - 1]` and `nums[r]`

- (3) Reverse the suffix: 
   Reverse the subarray `nums[l ... n - 1]` to get the lowest order for that suffix.

This ensures the next permutation is the smallest one that is **strictly greater** than the current configuration.


### Solution
```java
class Solution {
    public void nextPermutation(int[] nums) {
        if(nums.length == 1) return;

        int l = nums.length - 1, r = l;

        // Step 1: find the first index l such that nums[l - 1] < nums[l]
        while (l > 0 && nums[l - 1] >= nums[l]) {
            l--;
        }
         // If no such index found → array is in descending order
        if(l == 0){
            reverse(0,r,nums);
            return;
        }

        // Step 2: find the rightmost number greater than nums[l - 1]
        while(nums[r] <= nums[l-1]){
            r--;
        }
        
        swap(l-1, r, nums);
        reverse(l, nums.length-1, nums);
    }

    public void swap(int l, int r, int[] nums){
        int temp = nums[l];
        nums[l] = nums[r];
        nums[r] = temp;
    }

    public void reverse(int l, int r, int[] nums){
        while(l < r){
            swap(l, r, nums);
            l++;
            r--;
        }
    }
}
```

```
Time Complexity: O(N)
Space Complexity: O(1)
```