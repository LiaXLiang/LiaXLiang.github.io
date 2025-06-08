---
title: 1060 Missing Element in Sorted Array
date: 2025-06-08
categories: [Leetcode_Notes, Binary Search]
---
# I. Intuitive Approach

Since the input array *nums* is strictly increasing, we can iterate through it from left to right to directly find the k-th missing number. 

### 📌 Algorithm
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
### 📌 Algorithm
1. Check if the k-th missing number is beyond the array
   - First, calculate how many numbers are missing up to the last element of the array using ```missing(n - 1)```
   - If ```k > missing(n - 1)```, then the k-th missing number lies beyond the last element.
     - In that case, the answer is simply: ```nums[n−1] + (k − missing(n−1))```
2. Binary Search to Find the Correct Interval
   - If the k-th missing number is within the bounds of the array, we perform binary search to find the smallest index *i* such that: mising(i - 1) < k ≤ missing(i)
   - If ```missing(i) < k```, then the k-th missing number is **to the right of** index i.
   - If ```missing(i) >= k```, then it lies **to the left** or **exactly at** index i.
   - 