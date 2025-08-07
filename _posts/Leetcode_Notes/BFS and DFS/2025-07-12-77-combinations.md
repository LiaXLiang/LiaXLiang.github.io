---
title: 77. Combinations
date: 2025-07-12
categories: [Leetcode_Notes, BFS and DFS]
---

## How to Avoid Duplicate Combinations
We don't want both [1,2] and [2,1] — they represent the same combination. 

We can always build combinations in ascending order. This ensures that once a number has been used, we only choose larger numbers in subsequent steps.


We achieve this using a `start` variable in our DFS/backtracking loop.

## Visual Search Space (n = 4, k = 3)
```

Level 1 (start = ) |       1          |     2       |     3     |    4    |
                   | ↓     ↓     ↓    |   ↓   ↓     |     ↓     |    ↓    |
Level 2:           | 2     3     4    |   3   4     |     4     |    ✘    |
                   |/ \    ↓     ↓    |   ↓   ↓     |     ↓     |         |
Level 3:           |3 4    4     ✘    |   4   ✘     |     ✘     |         |
```
From each starting number *i*, we recursively choose larger values `j > i`.
This guarantees no repeated permutations (i.e., [2,1] can never occur).

## DFS Template Breajdown
Here's how the [general backtracking/DFS template]((https://liaxliang.github.io/17-letter-combinations-of-a-phone-number/)) maps to this problem:

### 3 Major Components
- `currentPath`
  - represents the current partial combination being constructed
  - `List<Integer> currentPath`
- `A list of remaining choices`
  -  We don’t store a list of remaining numbers directly. Instead, we use a `start` index to indicate which numbers are still available to choose.
  - e.g.,
    - On the first level, `start = 1`, so we can choose from 1 to n
    - On the next level, `start = i + 1` ensures that each new number is strictly larger than the previous 
- `A result list`
  - Holds all complete combinations of length k
  - `List<List<Integer>> res = new ArrayList<>();`

### Base Case: When to Terminate Recursion?
We stop recursion when we’ve selected exactly *k* numbers.
```java
if (currentPath.size() == k) {
    res.add(new ArrayList<>(currentPath));
    return;
}
```
- We should use `res.add(new ArrayList<>(currentPath));` instead of `res.add(currentPath);`:
  - In Java, `Lists` are **mutable** objects, meaning their content can be changed after creation.
  - Java uses reference semantics for objects.
        
    When we write:
    ```java
    res.add(currentPath);
    ```
    We are **NOT copying** the content of the `currentPath`. We are just saving a **pointer** to the *res*-list in memory. Later modifications to `currentPath` (like remove() in backtracking) will affect all previously added lists in `res` because they all point to the same object.
  - At the end of recursion, `currentPath` becomes empty (due to `remove()` calls). If we use `res.add(currentPath)`, since all entries in `res` reference the same `currentPath`, they **ALL** appear empty in the final result.
### Decision-Making and Recursive Exploration 
Each recursive step follows the pattern:
- Make a Decision
  - Choose a number *i* from the remaining range `[start, n]`  
  - `currentPath.add(i);`
- Recurse
  - Continue exploring the next level, only allowing numbers greater than *i*
- Undo the decision after recursion (backtrack)
  - We only undo the last number in backtracking because each recursive call only adds one new number to the end of the path. 
  - So to undo that specific decision, we just remove that last number — it's the only change made at the current recursion level.
  - `path.remove(path.size() - 1);`


### Solution
```java
class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(n, k, 1, new ArrayList<>(), res);
        return res;
    }

    void backtrack(int n, int k, int start,  List<Integer> currentPath, List<List<Integer>> res){
        //base case
        if(currentPath.size() == k){
            res.add(new ArrayList<>(currentPath));
            return;
        }
        for(int i = start; i <= n; i++){
            currentPath.add(i);  // make decision
            backtrack(n, k, i+1, currentPath, res);   // recurse
            currentPath.remove(currentPath.size() - 1); // undo
        }
    }
}
```