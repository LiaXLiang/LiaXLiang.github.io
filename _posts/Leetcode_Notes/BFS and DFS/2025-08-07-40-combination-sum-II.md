---
title: 40. Combination Sum II.
date: 2025-08-07
categories: [Leetcode_Notes, BFS and DFS]
---

## Core Idea

### Solution
//====== Marks the difference with Leetcode 49: Combination Sum II.
```java
class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        //=======================
        Arrays.sort(candidates);
        //=======================
        backtarck(new ArrayList(), 0, candidates, target, res);
        return res;

    }

    public void backtarck(List<Integer> path, int pos, int[] candidates, int target, List<List<Integer>> res){
        if(target == 0){
            res.add(new ArrayList(path));
            return;
        }

        for(int i = pos; i < candidates.length; i++){
            if(candidates[i] > target) continue;
            //=======================================================
            if(i > pos && candidates[i] == candidates[i-1]) continue;
            //=======================================================
            
            path.add(candidates[i]);
            backtarck(path, i+1, candidates, target - candidates[i], res);
            path.remove(path.size() - 1);
        }
    }
}
```