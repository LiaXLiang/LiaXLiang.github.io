---
title: 6. Zigzag Conversion
date: 2025-07-09
categories: [Leetcode_Notes, String]
---

## 📌 Algorithm 1: Mathematical Gap-Based Construction
### Core Idea
By analyzing the structure of the zigzag pattern, we can derive a precise mathematical rule that governs the placement of each character.

For example, consider a string of 25 characters with `numRows = 5`. The character **index layout** is as follows:

```
row0:       0       8        16        24
row1:        1     7 9      15 17     23
row2:         2   6   10   14   18   22
row3:          3 5     11 13     19 21
row4:           4       12         20
```

#### (1) Cycle Length
A cycle is one complete “V” movement in the Zigzag path. For any `numRows ≥ 2`, the indices pattern repeat every
```java
cycle = 2 × numRows − 2;
```
characters.

e.g., `numRows = 5 ⇒ cycle = 8` 

That means characters at indices 0, 8, 16, 24 appear in row 0 — one per cycle.

#### (2) Row-wise Index Pattern
The characters form a repeating visual pattern like this:
```
        *
 *     *   *  
  *   *
   * *
    *

```

```

        *
       *   *  
  *   *     *
   * *
    *

```


```

        *
       *  *  
      *    *
 *   *      *
    *

```

#### (3) Computing Spacing per Row
Suppose `numRows = R`, and we're constructing row `i` (0-indexed). 

Characters in row *i* are not evenly spaced — instead, they alternate between two different step sizes:
- firstSpace: number of steps to go down then up through the Zigzag
  -  `firstSpace  = 2 × (numRows − i − 1);`
- secondSpace: number of steps to go up then down (complement of the first)
  - `secondSpace = cycle − firstSpace;`


Special Cases:
- For the top row (i = 0): 
  - firstSpace = cycle;
  - secondSpace = 0 → only downward strokes
- For the bottom row (i = numRows − 1): 
  - firstSpace = 0;
  - secondSpace = cycle → only upward strokes
- For middle rows: alternate firstSpace, secondSpace, firstSpace, …


In summary: 
- `cycle = 2 * numRows - 2;`
- Each row can be constructed independently by jumping through the input string using `firstSpace` and `secondSpace` alternately. This approach eliminates the need to simulate the 2D grid or use extra memory.

### Solution
```java
class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1 || s.length() <= numRows) return s;

        int n = s.length();
        int cycle = 2 * numRows - 2; // One full Zigzag cycle (down + diagonal up)
        StringBuilder res = new StringBuilder(n);

        for (int row = 0; row < numRows; row++) {
            // For each row, calculate alternating step sizes
            int firstSpace = (numRows - row - 1) * 2;       // Downward-to-upward spacing
            int secondSpace = cycle - firstSpace;           // Upward-to-downward spacing
            int index = row;
            boolean toggle = true;                          // Toggles between firstSpace and secondSpace

            while (index < n) {
                res.append(s.charAt(index));

                // Handle edge rows with only one valid step
                if (firstSpace == 0) {
                    index += secondSpace;
                } else if (secondSpace == 0) {
                    index += firstSpace;
                } else {
                    index += toggle ? firstSpace : secondSpace;
                    toggle = !toggle; // Alternate between the two steps
                }
            }
        }

        return res.toString();
    }
}
```

```
Time Complexity: O(N)
Space Complexity: O(N)
```

## 📌 Algorithm 2: Simulate Zigzag Traversal
Instead of calculating character positions using mathematical formulas, we can simulate the actual writing process of the zigzag pattern.

- (1) Initialize a list of StringBuilder objects, one for each row:

  - `List<StringBuilder> rows = new ArrayList<>(numRows);`

- (2) Use an index *i* to track the current row, and a flag variable to indicate the current direction:
    - flag = +1 means moving downward through the rows.
    - flag = -1 means moving upward diagonally.

- (3) Iterate through each character *c* in the input string *s*, and do the following:
  - Append c to rows[i].
  - If `i == 0` or` i == numRows - 1`, reverse direction by flipping `flag = -flag;`.
  - Move to the next row by setting i += flag.

- (4) After processing all characters, concatenate all rows in order to form the final result.

### Solution
```java
class Solution{
    public String convert(String s, int numRows) {
        if(numRows == 1) return s;
        List<StringBuilder> rows = new ArrayList<>();
        for(int i = 0; i < numRows; i++) rows.add(new StringBuilder());
        
        int i = 0, flag = -1;
        for(char c : s.toCharArray()) {
            rows.get(i).append(c);
            if(i == 0 || i == numRows -1) flag = -flag; // change direction
            i += flag;
        }

        StringBuilder res = new StringBuilder();
        for(StringBuilder row : rows) res.append(row);
        return res.toString();
    }
}
```

```
Time Complexity: O(N)
Space Complexity: O(N)
```