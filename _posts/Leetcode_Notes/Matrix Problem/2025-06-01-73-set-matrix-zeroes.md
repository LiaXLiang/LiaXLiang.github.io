---
title: 73. Set Matrix Zeroes
date: 2025-06-01
categories: [Leetcode_Notes, Matrix Problem]
---
### Core Idea
We use the **first row** and **first column** of the matrix itself as markers to record which rows and columns should be set to zero. This allows us to achieve the desired transformation using constant extra space, with the exception of two boolean flags to track whether the first row or first column originally contains any zero.

- e.g. 
    ```
    Matrix A:
    Original:             After Marking:         Final Output:
    1  2  3  4             0  0  3  0             0  0  3  0
    5  0  7  8     ==>     0  0  7  8     ==>     0  0  0  0
    0  1  2  3             0  1  2  3             0  0  0  0
    3  4  5  0             0  4  5  0             0  0  0  0
    ```
    and 
    ```
    Matrix B: 
    Original:             After Marking:         Final Output:
    1  2  3  0             0  0  3  0             0  0  0  0
    5  0  7  8     ==>     0  0  7  8     ==>     0  0  0  0
    0  1  2  3             0  1  2  3             0  0  0  0
    3  4  5  0             0  4  5  0             0  0  0  0
    ```
    Although Matrices *A* and *B* differ only in the top-right element (*4* in Matrix *A* vs. *0* in Matrix *B*), their marker states become identical after the marking phase. However, because Matrix B’s top-right corner is 0, this causes the entire first row to be set to zero in the final step.
    
    The same logic applies to any zeros in the first column: if the first column contains any original zero, the entire column must also be zeroed at the end. Therefore, we need two additional boolean variables to explicitly track whether the first row or first column originally contains any zeros, as these positions are being reused to store marker information.

### Solution
```java
class Solution {
    public void setZeroes(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        boolean firstRowZero = false, firstColZero = false;

        // Step 1: Check first row and column
        for (int i = 0; i < row; i++){
            if (matrix[i][0] == 0){
                firstColZero = true; 
                break;
            }
        }  
        for (int j = 0; j < col; j++){
            if (matrix[0][j] == 0){
                firstRowZero = true; 
                break;
            } 
        }
        
        // Step 2: Mark rows and cols
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(matrix[i][j] == 0){
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        // Step 3: Apply zeros based on markers
        for(int i = 1; i < row; i++){
            if(matrix[i][0] == 0){
                for(int j = 1; j < col; j++){
                    matrix[i][j] = 0;
                }
            }
        }
        for(int j = 1; j < col; j++){
            if(matrix[0][j] == 0){
                for(int i = 1; i < row; i++){
                    matrix[i][j] = 0;
                }
            }
        }

        // Step 4: Zero out first row/column if needed
        if(firstRowZero){
            for(int j = 1; j < col; j++){
                matrix[0][j] = 0;
            }
        }
        if(firstColZero){
            for(int i = 1; i < row; i++){
                matrix[i][0] = 0;
            }
        }
    }
}
```

```
Time Complexity: O(M·N)
    - We traverse the whole matrix at most two times
Space Complexity: O(1)
```