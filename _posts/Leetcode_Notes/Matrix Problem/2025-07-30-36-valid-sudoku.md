---
title: 36. Valid Sudoku
date: 2025-07-30
categories: [Leetcode_Notes, Matrix Problem]
---

## Core Idea
The core requirement of this problem is to ensure no **repetition** of digits in:
- Each row
- Each column
- Each 3×3 sub-box

To verify these constraints, we can leverage the natural indexing power of arrays. We initialize three sets of data structures:

- `rows[9][9]`: tracks digits 1–9 in each row

- `cols[9][9]`: tracks digits 1–9 in each column

- `boxes[9][9]`: tracks digits 1–9 in each 3×3 box

We iterate through each cell in the `board` exactly once. For every non-empty cell:
- (1) Convert the character '1' to '9' into an integer index between 0 and 8.

- (2) Check whether this number has already appeared in the corresponding *row*, *column*, or *box*.

- (3) If it has, return false.

- (4) If not, mark its presence in the three corresponding arrays.

## Determining the 3x3 Box Index
How do we compute the index of the 3×3 box that a given cell `(i, j)` belongs to?

`int boxIndex = (i / 3) * 3 + j / 3;`
- `i / 3` gives the row block (0, 1, or 2)
- `j / 3` gives the column block (0, 1, or 2)
- Combining them ensures each box has a unique index from 0 to 8

### Solution
```java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        int[][] rows = new int[9][9];
        int[][] cols = new int[9][9];
        int[][] boxes = new int[9][9];

        // Traverse every cell in the board
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                char c = board[i][j];
                
                if (c == '.') continue;  // Skip empty cells

                int num = c - '1';  // Convert char '1'-'9' to index 0-8
                int boxIndex = (i / 3) * 3 + (j / 3);

                // Check for repetition in row, column, and box
                if (rows[i][num] == 1 || cols[j][num] == 1 || boxes[boxIndex][num] == 1) {
                    return false;
                }

                // Mark the number as seen
                rows[i][num] = 1;
                cols[j][num] = 1;
                boxes[boxIndex][num] = 1;
            }
        }

        return true;
    }
}
```
```
Time Complexity: O(1)

Although we're iterating through the entire board, the board size is fixed at 9×9, so:
    - We perform at most 81 iterations (9 rows × 9 columns).
    - Each cell operation (checking/setting in the row/column/box arrays) is done in constant time.

Space Complexity: O(1)

- rows[9][9], cols[9][9], and boxes[9][9] arrays — each of size 81 integers.
- These are fixed-size data structures (since Sudoku is always 9×9).
So the total space used is constant, and the space complexity is also O(1).
```