---
title: 1060 Missing Element in Sorted Array
date: 2025-06-08
categories: [Leetcode_Notes, Binary Search]
---
# I. Intuitive Approach

Since the input array *nums* is strictly increasing, we can iterate through it from left to right to directly find the k-th missing number. 

### 📌 Algorithm
Let ```n = nums.length```
We loop through the array and, for each index i in the range 1 ≤ i < n, we perform the following steps:
- Calculate **the number of missing elements** between ```nums[i - 1]``` and ```nums[i]```
  - If ```k ≤ missing```, it means the k-th missing number lies between ```nums[i - 1]``` and ```nums[i]```. 
    - In this case, we can return it directly as: ```return nums[i - 1] + k;```
  - Otherwise, the missing numbers in this range are not enough to reach the k-th missing element. We subtract the number of missing elements from *k*, and continue checking the next interval.
- If we finish the loop and still haven't returned, it means the k-th missing number lies beyond the last element of the array. In that case, we simply add k to the last element: ```return nums[n - 1] + k;```
  
### Solution
```java
class Solution {
    public int missingElement(int[] nums, int k) {
        for(int i = 1; i < nums.length; i++){
            int missing = nums[i] - nums[i-1] - 1;

            if (k <= missing) {
                return nums[i-1] + k;
            }

            k -= missing;
        }

        return nums[nums.length - 1] + k;
    }
}
```

```
Time Complexity: O(N)
Space Complexity: O(1)
```

<br>
<br>  
<br>

# II. Binary Search
### Core Idea: Use "the number of missing elements" to guide the search
We define a helper function to calculate how many numbers are missing between ```nums[0]``` and ```nums[i]```:
```java 
missing(i) = nums[i] - nums[0] - i;
```
```
Given nums = [5,8,9,11,20]
missing(4) = nums[4] - nums[0] - 4
           = 20 - 5 - 4 
           = 11
This means that between nums[0] = 5 and nums[4] = 20, there are 11 missing elements.
```
### Algorithm Logic
Let ```mid = left + (right - left) / 2```

1. If ```missing(mid) ≥ k```:
   - Then the k-th missing number lies **to the left of or at** index ```mid```. 
2. If ```missing(mid) < k```:
   - Then the k-th missing number lies **strictly to the right** of index ```mid```. 

Even when ```missing(mid) == k```, we do not stop immediately — we continue searching leftward because there might be earlier positions where the same number of missing elements first reaches *k*. We want the smallest index that satisfies the condition.

e.g.
```
nums = [4, 7, 9, 10]
k = 3
```
missing(2) == 3 and missing(3) == 3. That means both index *2* and *3* satisfy the condition missing(i) == 3.
The problem asks us to find the 3rd missing number, which lies before index 2, not after.

We perform binary search to find **the smallest index *i*** such that: 
**```mising(i - 1) < k ≤ missing(i)```**

### Solution
```java
class Solution {
    public int missingElement(int[] nums, int k) {
        int left = 0;
        int right = nums.length - 1;

        /* Case 1: 
         If k-th missing number is beyond the last element
        */
        if (k > countMissing(nums, right)) {
            return nums[right] + (k - countMissing(nums, right));
        }

        /* Case 2:
         Binary search for the smallest index where missing(i) >= k
        */
        while (left <= right) {
            int mid = left + (right - left) / 2; // Prevent overflow

            if (countMissing(nums, mid) >= k) {
                // Even if missing(mid) == k, we continue searching to the left
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        // At the end of loop: missing(left - 1) < k <= missing(left)
        return nums[left - 1] + (k - countMissing(nums, left - 1));
    }

    // Returns how many numbers are missing between nums[0] and nums[i]
    private int countMissing(int[] nums, int index) {
        return nums[index] - nums[0] - index;
    }
}
```

```
Time Complexity: O(log(N))
Space Complexity: O(1)
```