---
title: 70. Climbing Stairs
date: 2025-07-02
categories: [Leetcode_Notes, Dynamic Programming]
---
# Dynamic Programming
- **Step 1: Visualize Examples**
  ```
  ┌─  : one step at a time

  ┌─┘ : two steps at a time
  ```

  - f(1):      ┌─

  - f(2):      
    - ┌─┌─ 
    - ┌─┘

  - f(3):      
    - f(2) + ┌─    
    - f(1) + ┌─┘

  - f(4):
    - f(3) + ┌─
    - f(2) + ┌─┘
  
  - f(5):
    - f(4) + ┌─
    - f(3) + ┌─┘  
- ...
 
    Last-Move Analysis:
        
    When n ≥ 3, ignore the early choices and examine only the final move that lands us on step *n*:

    - Last Move = single step ┌─
        
        We must have stood on step *n-1* a moment earlier. The number of distinct ways to reach step *n-1* is **f(n-1)**.

    - Last Move = double steps  ┌─┘
       
        We must have stood on step *n-2* just before the jump. There are **f(n-2)** distinct ways to reach step *n-2*.

    The two sets of paths are **mutually exclusive** - no path can end with both a 1-step and a 2-step simultaneously.

- **Step 4: Generalize the Relationship, i.e., find the State Transition Formula**
   - F(n) = F(n−1) + F(n−2), if n ≥ 3
  
This mirrors the Fibonacci sequence and underpins the iterative solution.

### Solution
```java
class Solution {
    public int climbStairs(int n) {
        if(n <= 2){
            return n;
        }

        int p = 1;  //f(1)
        int q = 2;  //f(2)
        int r = 0;

        for(int i = 3; i <= n; i++){
            r = q + p;
            p = q;
            q = r;
        }

        return r;
    }
}
```

```
Time Complexity: O(N)
Space Complexity: O(1)
```