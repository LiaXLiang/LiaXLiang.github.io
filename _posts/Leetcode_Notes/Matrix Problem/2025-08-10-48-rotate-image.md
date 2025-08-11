---
title: 48. Rotate Image
date: 2025-08-10
categories: [Leetcode_Notes, Matrix Problem]
---

## Core Idea
The rotation can be decomposed into concentric layers, starting from the outermost layer and moving inward. For each layer, we perform a cyclic rotation of four elements at a time.

### Key Observations

- Layered Rotation: The matrix consists of square layers, with the outermost layer rotating first, followed by inner layers.

- Quadruple Cycles: Within each layer, rotation is achieved by swapping groups of four elements that form a cyclic dependency.



### Step-by-Step Process
<figure>
  <img src="https://raw.githubusercontent.com/LiaXLiang/LiaXLiang.github.io/master/assets/img/Leetcode_Notes/leetcode48.jpeg">
</figure>

**Outer Layer**:
   ```
   1    2    3    4
   5              8
   9              12
   13   14   15   16
   ```


   We start from the top-left (0,0) of the outer layer and process each **quadruple**:
   1. First quadruple
      1 → 4 → 16 → 13 → 1

      Indices: (0,0) → (0,3) → (3,3) → (3,0) → (0,0)
   2. Second quadruple
      2 → 8 → 15 → 9 → 2

      Indices: (0,1) → (1,3) → (3,2) → (2,0) → (0,1)
   3. Third quadruple
      3 → 12 → 14 → 5 → 3

      Indices: (0,2) → (2,3) → (3,1) → (1,0) → (0,2)

**Inner Layer**:

   We then process the inner 2×2 matrix:
   ```
   6   7
   10  11
   ```
   Following the same 4-way swap rule.

### Generalizing the Rotation

For any cell at position `(a, b)` in an `n x n` matrix, its new position after a 90-degree clockwise rotation follows this pattern:

- (a, b) moves to (b, n - 1 - a)
- (b, n - 1 - a) moves to (n - 1 - a, n - 1 - b)
- (n - 1 - a, n - 1 - b) moves to (n - 1 - b, a)
- (n - 1 - b, a) moves back to (a, b)

This forms a 4-way cycle, allowing us to rotate the matrix in-place by iterating through each layer and performing these swaps.

### Algorithm
1. Iterate through layers: 
   
   For each layer from 0 to n / 2.
   - Why only go up to n / 2?
      - Each layer consumes two rows and two columns (top+bottom, left+right).

      - Once we've processed half the rows, we’ve also processed half the columns — meaning we’ve covered all rings without overlap.

      - For odd 𝑛, the middle cell is a single element and does not need rotation.

2. Iterate within a layer: 

   For each element in the current layer, perform 4-way swap. 
   
   - For each layer i, we process elements starting from the top-left corner `(i, i)` and move rightwards along the top edge of the ring.
   - However, we exclude the last column of the top edge (i.e., j goes from i to n - 1 - i), because the last element in the top edge (`(i, n - 1 - i)`) is part of the first 4-way swap and will be handled automatically. 

### Solution
```java
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i = 0; i < n / 2; i++) {
            for (int j = i; j < n - 1 - i; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[n - 1 - j][i];
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j];
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i];
                matrix[j][n - 1 - i] = tmp;
            }
        }
    }
}
```

```
Time Complexity: O(N^2)
Space Complexity: O(1)
```