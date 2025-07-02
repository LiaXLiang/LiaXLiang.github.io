---
title: 994. Rotting Oranges
date: 2025-05-20
categories: [Leetcode_Notes, BFS and DFS]
---
We solve this problem using BFS starting *simultaneously* from **all initially rotten oranges at minute 0**.

### 📌 Algorithm
- (1) Initialize the Queue with Rotten Oranges (Minute 0):
    - Traverse the grid and enqueue the positions of all initially rotten oranges. These serve as the BFS starting points. 
  
- (2) BFS Traversal – Spread the Rot Layer by Layer:
    - For each orange in the queue, dequeue it and explore its four neighboring cells (up, down, left, right).
    - If a neighboring cell contains a fresh orange, it becomes rotten. Enqueue this new rotten orange into the queue for the next round
    - At the end of each BFS level (i.e., after processing all oranges of the current minute), increment the minute counter.
- (3) Repeat Until the Queue is Empty:
    - Continue the BFS process level by level. Each level represents the spread of rot during that minute.
- (4) Final Check and Result:
    - After the BFS completes (queue becomes empty), check if there are any remaining fresh oranges in the grid.
    - If yes, return -1 (some oranges cannot be reached).
    - Otherwise, return the total number of minutes taken to rot all oranges.


### Solution
{% raw %}
```java
class Solution {
    public int orangesRotting(int[][] grid) {
        Queue<int[]> queue = new LinkedList<>(); 
        int rows = grid.length, cols = grid[0].length;
        int minutesElapsed = 0;

        // Step 1: Add all initially rotten oranges to the queue
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 2) {
                    queue.offer(new int[]{i, j});
                }
            }
        }

        // Step 2: Perform BFS level-by-level
        while (!queue.isEmpty()) {
            int size = queue.size();
            int newlyInfected = 0;

            for (int i = 0; i < size; i++) {
                int[] coordinate = queue.poll();
                newlyInfected += explore(grid, coordinate, queue);
            }

            // Only increment time if at least one new orange was infected this round
            if (newlyInfected > 0) {
                minutesElapsed++;
            }
        }

        // Step 3: Check if any fresh orange remains
        for (int[] row : grid) {
            for (int cell : row) {
                if (cell == 1) {
                    return -1;
                }
            }
        }

        return minutesElapsed;
    }


    public int explore(int[][] grid, int[] coordinate, Queue<int[]> queue){
        int r = coordinate[0], c = coordinate[1];
        int rows = grid.length, cols = grid[0].length;
        int changed = 0;

        // 4 directions
        int[][] dirs = {{-1,0}, {1,0}, {0,-1}, {0,1}}; 
        for (int[] dir : dirs) {
            int nr = r + dir[0];
            int nc = c + dir[1];

            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                if (grid[nr][nc] == 1) {
                    grid[nr][nc] = 2;
                    queue.offer(new int[]{nr, nc});
                    changed++;
                }
            }
        }
        return changed;
    }
}
```
{% endraw %}