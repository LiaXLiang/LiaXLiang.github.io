---
title: 509. Fibonacci Number
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
- **Step 1: Visualize Examples**
    - fib(0) = 0
    - fib(1) = 1
    - fib(2) = fib(0) + fib(1) = 0 + 1 = 1
    - fib(3) = fib(1) + fib(2) = 1 + 1 = 2
    - fib(4) = fib(2) + fib(3) = 1 + 2 = 3
    - fib(5) = fib(3) + fib(4) = 2 + 3 = 5
    - fib(6) = fib(4) + fib(5) = 3 + 5 = 8
    - fib(7) = fib(5) + fib(6) = 5 + 8 = 13
    - fib(8) = fib(6) + fib(7) = 8 + 13 = 21
- **Step 2: Find an Appropriate Subproblem**
    
    Break the full problem — computing `fib(n)` into smaller, repeatable subproblems, such that the solution to the overall problem depends only on the solutions to its subproblems.
    - To compute `fib(n)`, we only need two previous Fibonacci numbers: `fib(n-1)` and `fib(n-2)`. And recursively, `fib(n-2)`, `fib(n-3)`, ..., down to base cases `fib(1)` and `fib(0)`
    - The subproblem is: `F(k)` for any `k < n`.
- **Step 3: Find Relationships Among Subproblems**
    - `fib(k) = fib(k - 1) + fib(k - 2)`
- **Step 4: Generalize the Relationship, i.e., find the State Transition Formula**
  - F(n) = 0, if n = 0
  - F(n) = 1, if n = 1
  - F(n) = F(n−1) + F(n−2), if n ≥ 2
   
   Given that `F(n)` depends only on the two preceding terms, we can optimize the space by maintaining only three variables rather than an entire DP table.
- **Step 5: Implement by Solving Subproblems in Order**
  - We implement the recurrence iteratively from 2 → n, keeping track of the last two Fibonacci numbers.


### Solution
```java
class Solution {
    public int fib(int n) {
        if (n < 2) return n;

        int prevPrev = 0; // F(0)
        int prev = 1;     // F(1)
        int cur = 0;

        for (int i = 2; i <= n; i++) {
            cur = prev + prevPrev;
            prevPrev = prev;
            prev = cur;
        }

        return cur;
    }
}
```
```
Time Complexity: O(N)
Space Complexity: O(1)
``` 
