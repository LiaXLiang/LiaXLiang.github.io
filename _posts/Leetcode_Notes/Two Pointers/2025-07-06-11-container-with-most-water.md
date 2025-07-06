---
title: 11. Container With Most Water
date: 2025-07-06
categories: [Leetcode_Notes, Two Pointers]
---

### Geometry Behind the Problem
Suppose we select two lines at indices i and j (with i < j). These lines form the two vertical borders of a container. The amount of water the container can hold is determined by:

`Area(𝑖,𝑗) = min(height[𝑖], height[𝑗]) × (𝑗−𝑖)`

- `min(height[i], height[j])` is the height of the water (limited by the shorter line).

- `(j - i)` is the width of the base (distance between the two lines).


Let’s say we're at indices *i* and *j*:
- Moving either pointer inward reduces the width by 1.
- Now consider:
  - If we move the **taller** line inward:
    - The **height** is either **the same** or **lower**. 
    - the new area must be smaller.
  - If we move the **shorter** line inward:
    - The height might increase or decrease. 
    - A higher minimum height could lead to a larger area.
    - So, this move has the potential to improve the result.
  
Hence, to maximize area, we always move the pointer pointing to the **shorter** line.

### 📌 Algorithm
- (1) Initialize `left = 0`, `right = height.length - 1`
- (2) Initialize `maxArea = 0`
- (3) While left < right:
  - Compute the area between *left* and *right*
  - Update *maxArea* if needed
  - Move the pointer pointing to the **shorter** line inward
- (4) Return maxArea

### Solution
```java
class Solution {
    public int maxArea(int[] height) {
        int l = 0, r = height.length - 1;
        int maxArea = 0;
        // 'move' always points to the shorter line between height[l] and height[r]

        int move = 0;  

        while(l < r){
            move = (height[l] >= height[r]) ? r : l;
            maxArea = Math.max(maxArea, height[move] * (r - l));

            if(move == r){
                r--;
            }else{
                l++;
            }
        }
        return maxArea;
    }
}
```

```
Time Complexity: O(N)
Space Complexity: O(1)
```