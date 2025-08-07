---
title: 39. Combination Sum
date: 2025-08-07
categories: [Leetcode_Notes, BFS and DFS]
---

### Solution
```java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(candidates, target, 0, new ArrayList<>(), res);
        return res;
    }

    private void backtrack(int[] candidates, int target, int start, List<Integer> path, List<List<Integer>> res) {
        if (target == 0) {
            res.add(new ArrayList<>(path));
            return;
        }

        // Iterate over the candidates starting from index 'start'
        for (int i = start; i < candidates.length; i++) {
            // If the current number is greater than the remaining target, skip it
            if (candidates[i] > target) continue;

            // Choose the current number (add it to the current combination)
            path.add(candidates[i]);
            // Recurse with the updated target (target - current number)
            // We pass 'i' as 'start' to allow repeated use of the current candidate
            backtrack(candidates, target - candidates[i], i, path, res);
            // Backtrack by removing the last added number from the combination
            path.remove(path.size() - 1);
        }
    }
}
```