---
title: 509 Fibonacci Number
date: 2025-06-09
categories: [Leetcode_Notes, Dynamic Programming]
---
# I. Recursive Approach
### Solution
```java
class Solution {
    public int fib(int n) {
        if(n < 2) return n;
        return fib(n-1) + fib(n-2);
    }
}
```
```
Time Complexity: O(2^N)
- This implementation computes fib(n) using a top-down naive recursion without memoization. Each call to fib(n) results in two recursive calls: fib(n - 1) and fib(n - 2).
- As a result, the recursion tree grows exponentially in size:
The number of nodes (function calls) in the recursion tree is proportional to 2^N.

Space Complexity: O(N)
- Although the total number of calls is exponential, the maximum depth of the recursion stack is determined by the longest path in the recursion tree.
- This path corresponds to the sequence:
fib(n) → fib(n - 1) → fib(n - 2) → ... → fib(1)
There are n such nested calls before reaching the base case. 
```

<br>
<br>  
<br>

# II. Dynamic Programming
1. Step 1: Define the ```dp``` Array and the Meaning of Its Indices
   - We define ```dp[i]``` as the i-th Fibonacci number, i.e., `dp[i] = F(i)`

    However, in the final implementation, we do not explicitly use a `dp` array to save space. Instead, we use *three* variables to simulate the transitions in-place.
    Conceptually, we treat: `dp[i] = dp[i - 1] + dp[i - 2]` with the following correspondences:   
    - `p = dp[i - 2]`
    - `q = dp[i - 1]`
    - `r = dp[i]`
2. Step 2: Identify the State Transition Formula
    - `dp[i] = dp[i - 1] + dp[i - 2]`
3. Step 3: Initialize the ```dp``` Array
    - The base cases are: `dp[0] = 0`, `dp[1] = 1`
4. Step 4: Determine the Iteration Order 
    - Since the recurrence depends on `dp[i - 1]` and `dp[i - 2]`, we must compute the values in ascending order from 2 up to n.
5. Step 5: Use an Example to Simulate the `dp` Array
   ```
   e.g. Trace the computation for fib(5):
    Initialization: p = 0, q = 0, r = 1

    i = 2 → p = 0, q = 1, r = 1     → dp[2] = 1
    i = 3 → p = 1, q = 1, r = 2     → dp[3] = 2
    i = 4 → p = 1, q = 2, r = 3     → dp[4] = 3
    i = 5 → p = 2, q = 3, r = 5     → dp[5] = 5

### Solution
```java
class Solution {
    public int fib(int n) {
        if(n < 2) return n;

        int p = 0, q = 0, r = 1;
        for(int i = 2; i <= n; i++){
            p = q;
            q = r;
            r = p + q;
        }
        return r;
    }
}
```
```
Time Complexity: O(N)
Space Complexity: O(1)
``` 
