---
title: 53. Maximum Subarray
date: 2025-08-27
categories: [Leetcode_Notes, Dynamic Programming]
---


## Core Idea
### The central challenge is:

How can we maintain the starting position of a potential subarray, and when should we discard the current subarray in favor of a new one?

### The decision hinges on the running sum (curSum):

If `curSum` is positive:
- Even when we encounter a negative number, it is still beneficial to keep the current subarray.
- The reason is that the accumulated positive sum can absorb small negatives and still lead to a larger total if bigger positives come later.
    - Example: `[5, -2, 3]` → Keeping 5 - 2 still makes sense, because adding +3 yields a larger result.

If `curSum` is negative:
- There is no benefit in keeping it, because adding it to any future element will only make that sum smaller.
- At this point, we should discard the current subarray and start a new one from the next element.

    - Example: `[-4, 2, 5]` → Keeping -4 only reduces the result. It’s better to restart at 2.

This greedy choice ensures that at each index we decide whether to extend the current subarray or restart from the current element

## 📌 Algorithm 
1. Initialize two variables:
    - `curSum = nums[0]` → current running sum
    - `maxSum = nums[0]` → maximum sum found so far
2. Iterate through the array from index *1* to *n-1*:
    - Update `curSum`:
        
        - `curSum = (curSum < 0) ? nums[i] : curSum + nums[i];`
        - This expresses the decision: extend the current subarray (`curSum + nums[i]`) or restart from the current element (`nums[i]`).
    - Update `maxSum`:
        - `maxSum = max(maxSum,curSum)`
3. Return `maxSum`

### what happens if the array contains only negative numbers?

For example: [-20, -10, -30, -100, -1].
Since we initialize both `curSum` and `maxSum` with the first element, the algorithm still works correctly. Although `curSum` may be updated to other negative values as we iterate, `maxSum` always records the largest value observed so far.

Thus, the final result will simply be the largest (least negative) number in the array, which is indeed the correct maximum subarray sum in the all-negative case.

### Solution
```java
class Solution {
    public int maxSubArray(int[] nums) {
        int curSum = nums[0], maxSum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            curSum = (curSum < 0) ? nums[i] : curSum + nums[i];
            maxSum = (curSum > maxSum) ? curSum : maxSum;
        }
        return maxSum;
    }
}
```

```
Time Complexity: O(N)
Space Complexity: O(1)
```