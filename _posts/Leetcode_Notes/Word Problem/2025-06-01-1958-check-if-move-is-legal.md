---
title: 1958 Check if Move is Legal
date: 2025-06-01
categories: [Leetcode_Notes, Word Problem]
---

### 📌 Algorithm
The core logic of this problem is not particularly complex. We simply need to enumerate all 8 possible directions and, for each direction, perform the following checks:

- (1) The immediate next cell in that direction:
    - must be **within the board boundaries**, and
    - must contain **the opposite color** of the input color.

- (2) From the second cell onward (i.e., two steps from the starting point), we continue moving in the same direction, and:
    - we must not go out of bounds,
    - we must not encounter an empty cell (.),
    - until we eventually reach a cell that contains a piece of the same color as color.

- (3) If such a cell is found while satisfying all the above conditions, then the move is valid, and we return true.

### Implementation Note
The key is how to implement this efficiently and cleanly.
- A common and elegant trick is to define all 8 movement directions using a static constant array:
    ```java
    private static final int[][] DIRS = {
        {1, 0}, {1, 1}, {0, 1}, {-1, 1},
        {-1, 0}, {-1, -1}, {0, -1}, {1, -1}
    };
    ```
    Using private static final has clear advantages:
    - ```private```: Ensures encapsulation. The direction array can only be accessed within the ```Solution class``` and cannot be modified externally.
    - ```static```: The direction array is associated with the class itself rather than any instance. This means it is only initialized once in memory, which saves space and avoids unnecessary reallocation for each function call or object instantiation.
    - ```final```: Marks the reference as immutable, preventing it from being reassigned to another array. While the contents of the array can still be modified, using final communicates the intention that this array should remain unchanged.
- XOR Trick for Opponent's Color
    - An optimization is to compute the opponent’s color using XOR:
        ```java
        color ^ 'B' ^ 'W'
        ```
    This works because ```'B' ^ 'W'``` is a fixed value. So:
    - If color == 'B', then 'B' ^ 'B' ^ 'W' → 'W'
    - If color == 'W', then 'W' ^ 'B' ^ 'W' → 'B'

### Solution
```java
class Solution {
    private static final int[][] DIRS = {{1,0},{1,1},{0,1},{-1,1},
                                         {-1,0},{-1,-1},{0,-1},{1,-1}};
       
    public boolean checkMove(char[][] board, int rMove, int cMove, char color) {
        // Iterate through each direction vector in DIRS.
        for (int[] dir : DIRS){
            int x = rMove + dir[0];
            int y = cMove + dir[1];

            /* This if-statement checks:
               - Whether the adjacent cell in the current direction is within the board;
               - And whether it contains the oposite color
            */
            if(x < 0 || x > 7 || y < 0 || y > 7 || board[x][y] != (color ^ 'B' ^ 'W')){
                continue;
            }

            // Continue moving in the current direction to examine the next cells.
            while(true){
                x += dir[0];
                y += dir[1];

                // If the position is out of bounds or reaches an empty cell,
                // this direction cannot form a valid capture; break the loop.
                if (x < 0 || x > 7 || y < 0 || y > 7 || board[x][y] == '.') {
                    break;
                }

                // If after traversing opponent's pieces we reach one of our own,
                // a valid capture is formed; return true.
                if (board[x][y] == color) {
                    return true;
                }
            }
        }
        // No valid direction found for capture; return false.
        return false;
    }
}
```

```
Time Complexity: O(M+N)
M := the number of rows in the board
N := the number of columns in the board

We iterate over 8 directions. In each direction, in the worst case, we may need to walk all the way across the board, checking one cell at a time - that is, up to O(M) steps vertically or O(N) steps horizontally (or diagonally, which is bounded by min(M, N)).
Thus, the worst-case time complexity is: O(8⋅max(M,N))=O(M+N)

Space Complexity: O(1)
We use only a constant-sized array DIRS to represent 8 directions: int[8][2]. Hence, space complexity is also constant. 
```