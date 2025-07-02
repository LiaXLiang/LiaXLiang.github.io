---
title: 151 Reverse Words in a String
date: 2025-07-02
categories: [Leetcode_Notes, Two Pointers]
---

### Core Idea
We treat each word as a block and traverse the string from right to left. Our goal is to extract words one by one in reverse order and rebuild the result string.

To do this, we use two pointers: *right* and *left* to locate the boundaries of each word:
- *right*: scans backward to skip over trailing spaces and lands on the last character of a word.
- *left*: scans backward from right to find the first space character (or the beginning of the string), marking the start of the word.

Once the word boundary [left + 1, right] is identified, we append the substring to our result.

This process repeats until the entire string is traversed.

### Solution

```java
class Solution {

    public String reverseWords(String s) {

        // Result buffer — StringBuilder is more efficient than repeated "+"
        StringBuilder result = new StringBuilder();

        // `right` starts at the end of the string and scans leftward
        for (int right = s.length() - 1; right >= 0; right--) {

            // 1) Skip trailing spaces
            if (s.charAt(right) == ' ') {
                continue;
            }

            // 2) Move `left` to the first space (or -1) to find the word start
            int left = right;
            for (; left >= 0; left--) {
                if(s.charAt(left) == ' '){
                    break;
                }
            }

            /*
             * 3) The word spans (left, right] — substring is left-inclusive/right-exclusive:
             *      start = left + 1
             *      end   = right + 1
             */
            result
                .append(s, left + 1, right + 1) // append the current word
                .append(' ');                   // add a space separator

            // 4) Continue scanning from the character before this word
            right = left;
        }

        // Remove the extra trailing space
        result.setLength(result.length() - 1);

        return result.toString();
    }
}
```

```
Time Complexity: O(N)
    Each char visited once; append() is linear

Space Complexity: O(N)
	For the output string stored in StringBuilder
```

### Implementation Notes
#### 1. Why do we use `StringBuilder` instead of `String res = ""` with `res = res + word`?
Strings in Java are immutable, which means that every time we do `res = res + word`, Java internally creates a brand-new String, copies all characters from `res` and `word`, and then discards the old `res`.

`StringBuilder` is a **mutable buffer** optimized for exactly this case: building up a string piece by piece. The `append()` method simply writes into the existing buffer or, if necessary, expands it with O(1) cost, no intermediate `String` objects are created until the final `toString()` call.

#### 2. A Practical Illustration of `break` vs `continue`
-  `continue`: Skip and Move On
    
    We use the *right* pointer to skip any trailing spaces and locate the end of a word by scanning leftward.
    
    Here, we apply *continue* when we encounter spaces — they are not part of the word, so we skip this iteration and let the loop keep scanning:

    ```java
    if (s.charAt(right) == ' ') {
        right--;
        continue; // temporarily skip; not the word yet
    }
    ```

    As soon as a non-space character is found, we stop skipping and proceed with the next logic — extracting the word. 
    
    `continue` is used when the condition is not ready, and we need to keep searching.

- `break`: Condition Met, Exit Immediately
    
    Once we’ve identified the end of a word (via *right*), we then use the *left* pointer to find the start of the word.

    This time, we scan leftward until we hit a space or reach the beginning of the string.

    As soon as we encounter a space, we know the word has ended — so we exit the loop immediately using break.

    ```java
    for (left = right; left >= 0; left--) {
        if (s.charAt(left) == ' ') {
            break; // word boundary found, stop here
        }
    }
    ```
    `break` is used when the goal is reached, and we can stop immediately.

