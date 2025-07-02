---
title: 1953. Maximum Number of Weeks for Which You Can Work
date: 2025-05-30
categories: [Leetcode_Notes, Word Problem]
---

### Intuition
This is essentially a scheduling problem with a key restriction: We may not work on the same project in two consecutive weeks.

Let’s say Project *A* has many more tasks than the others.
- If we try to alternate between Project *A* and the rest (e.g., A–X–A–Y–A–Z...), then each "non-A project" acts as a buffer or interleaving slot.

- But what if there aren’t enough of these other projects to interleave with A?
  
Then, eventually, we'll be forced to repeat Project *A* in consecutive weeks — which is not allowed.

Therefore, the main question becomes: Are there enough tasks in the other projects to interleave with the dominant project?

### Mathematical Modeling
Let’s define the following:
- ```total``` = total number of tasks = sum(milestones)
- ```max``` = maximum number of tasks in a single project = max(milestones)

- ```rest``` = total number of tasks in **all other** projects = total - max

### Case Analysis
- Case 1: rest ≥ max - 1
    - If the combined task count of **all other** projects is at least max - 1
    - → There are enough “gaps” to alternate between the max project and the others.
    - → We can execute a pattern like: A-X-A-X-A-Y…
    - Result: we can complete **all total tasks** without violating the constraint.

- Case 2: rest < max - 1
    - If other projects cannot provide enough interleaving tasks,
    - → We can alternate at most ```rest``` times.
    - → After that, we'll have ```max - rest - 1``` tasks from the *max* project left unexecuted (because they would violate the “no two consecutive weeks” rule).
    - Result: We can complete at most ```rest * 2 + 1``` weeks:  *rest A-X pairs* + *one final standalone A*.

### Solution
```java
class Solution {
    public long numberOfWeeks(int[] milestones) {
        long total = 0;
        int max = 0; 
        for (int m : milestones) {
            total += m;
            max = Math.max(max, m);
        }

        if (max <= total - max) {
            return total;
        } else {
            return 2 * (total - max) + 1;
        }
    }
}
```

### Key Insight
This is a classic greedy strategy problem:
- We always want to use the most frequent task as often as possible,
- But only if we can safely interleave it with others to avoid violating the rules.

The trick is to recognize when that’s possible — and when it’s not.



