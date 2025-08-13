---
title: 40. Combination Sum II
date: 2025-08-07
categories: [Leetcode_Notes, BFS and DFS]
---

## Core Idea
We begin by sorting the array, which ensures that we can easily identify if adjacent elements are identical.  

1. Allow Duplicates in the Vertical Direction:
   - The vertical direction refers to the deeper recursive calls. At each level of recursion, it is allowed to use the same number. For example, when we are choosing a number, in the next recursive call, we can still use the same number at the next position.
   - `backtarck(path, i+1, candidates, target - candidates[i], res)` means that when recursively moving to the next level, `i` is incremented to `i+1`, which allows the same number to be used only once in each combination.
2. Disallow Duplicates in the Horizontal Direction:
   - The horizontal direction refers to recursion at the same level, where we skip over duplicate numbers to avoid generating duplicate combinations.
   - `if (i > pos && candidates[i] == candidates[i - 1]) continue;` ensures that if the current element is the same as the previous element at the same recursion level, we skip the current element, avoiding duplicate combinations.
     - `i > pos` ensures that we only skip duplicate elements at the same recursion level (i.e., horizontal direction). 
     - `candidates[i] == candidates[i - 1]` ensures we skip the current element if it is the same as the previous element, thus avoiding duplicate combinations.

### Solution
`//======` marks the difference with [Leetcode 49: Combination Sum II](https://liaxliang.github.io/39-combination-sum/).
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