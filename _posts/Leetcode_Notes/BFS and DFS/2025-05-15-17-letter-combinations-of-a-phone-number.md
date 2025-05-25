---
title: 17 Letter Combinations Of A Phone Number
date: 2025-05-15
categories: [Leetcode_Notes, BFS and DFS]
---

# I. BFS Queue-Based Approach

### We treat the process of building combinations as a breadth-first traversal: 
- Each digit adds a new "layer" of characters to all current strings.
- A queue helps track and generate combinations at each layer.
  
### 📌 Algorithm Steps
  - (1) Initialize the Queue:
    - Start with a queue containing an empty string: [""].
  - (2) Iterate through each digit in the input:

    - Retrieve the corresponding letter set from the digit-to-letters map.

    - For each existing partial combination in the queue (based on the current queue size), extend it by appending every letter in the current letter set.
  
    - Enqueue the newly formed combinations.
  - 
    e.g. digits = "249 with mapping:  
            &nbsp;&nbsp;&nbsp;&nbsp; 2 → abc  
            &nbsp;&nbsp;&nbsp;&nbsp; 4 → ghi  
            &nbsp;&nbsp;&nbsp;&nbsp; 9 → wxyz
        


    ```text
        **Step 0: Initialize**

        Queue: [""]
        -----------------------------------------------------------

        **Step 1: Process digit = '2' → letters = "abc"**
        
        Initial queue size = 1
        Dequeue "" and append each letter in "abc": → "a", "b", "c"
        Updated Queue: ["a", "b", "c"]
        -----------------------------------------------------------

        **Step 2: Process digit = '4' → letters = "ghi"**
        Initial queue size = 3
        Dequeue each item and append every letter in "ghi":

        "a" → "ag", "ah", "ai"  
        "b" → "bg", "bh", "bi"  
        "c" → "cg", "ch", "ci"  

        Updated Queue:  
        ["ag", "ah", "ai", "bg", "bh", "bi", "cg", "ch", "ci"]
        -----------------------------------------------------------

        **Step 3: Process digit = '9' → letters = "wxyz"**
        Initial queue size = 9
        Dequeue each item and append every letter in "wxyz":

        "ag" → "agw", "agx", "agy", "agz"  
        "ah" → "ahw", "ahx", "ahy", "ahz"  
        "ai" → "aiw", "aix", "aiy", "aiz"  
        "bg" → "bgw", "bgx", "bgy", "bgz"  
        "bh" → "bhw", "bhx", "bhy", "bhz"  
        "bi" → "biw", "bix", "biy", "biz"  
        "cg" → "cgw", "cgx", "cgy", "cgz"  
        "ch" → "chw", "chx", "chy", "chz"  
        "ci" → "ciw", "cix", "ciy", "ciz"

        Final Queue: 9 × 4 = 36 combinations
    ```

### Solution
 ```java
    import java.util.*;

    class Solution {
        public List<String> letterCombinations(String digits) {
            if (digits == null || digits.length() == 0) {
                return new ArrayList<>();
            }

            // Digit-to-letters mapping (index corresponds to digit)
            String[] phone = {
                "",     // 0
                "",     // 1
                "abc",  // 2
                "def",  // 3
                "ghi",  // 4
                "jkl",  // 5
                "mno",  // 6
                "pqrs", // 7
                "tuv",  // 8
                "wxyz"  // 9
            };

            Queue<String> queue = new LinkedList<>();
            queue.offer("");

            int digitCount = digits.length();

            for (int i = 0; i < digitCount; i++) {
                int nextDigit = digits.charAt(i) - '0';
                String letters = phone[nextDigit];
                int size = queue.size();


                // Expand each existing combination by appending letters of next digit
                for (int j = 0; j < size; j++) {
                    String combination = queue.poll();

                    for (int k = 0; k < letters.length(); k++) {
                        queue.offer(combination + letters.charAt(k));
                    }
                }
            }

            return new ArrayList<>(queue);
        }
    }
```
```
**Time Complexity:** O(3^M * 4^N)

**Space Complexity:**  O(3^M * 4^N)

Where:  
- M: number of digits mapping to 3 letters  
- N: number of digits mapping to 4 letters  
```

**<font color = red> Implementation Notes </font>**
#### Why capture the current queue size before expansion?
- This isolates processing to the existing combinations before expanding with the new digit's letters. It prevents mixing newly added items from the same round.

<br>
<br>  
<br>

# II. DFS Recursive Backtracking
Instead of expanding the tree level by level (as in breadth-first search), we use a depth-first approach by exploring each path down to the leaf before backtracking.
    
### Solution 

```java
import java.util.*;

class Solution {
    public List<String> letterCombinations(String digits) {
        if (digits == null || digits.length() == 0) {
            return new ArrayList<>();
        }

        Map<Character, String> phone = new HashMap<>();
        phone.put('2', "abc");
        phone.put('3', "def");
        phone.put('4', "ghi");
        phone.put('5', "jkl");
        phone.put('6', "mno");
        phone.put('7', "pqrs");
        phone.put('8', "tuv");
        phone.put('9', "wxyz");
        
        List<String> combinations = new ArrayList<>();

        backtrack(phone, combinations, digits, "");
        return combinations;
    }

    public void backtrack(
        Map<Character, String> phone,
        List<String> combinations,
        String remainingDigits,
        String currentPath
    ) {
        if (remainingDigits.isEmpty()) {
            combinations.add(currentPath);
            return;
        }

        char currentDigit = remainingDigits.charAt(0);
        String letters = phone.get(currentDigit);

        for (char letter : letters.toCharArray()) {
            backtrack(
                phone,
                combinations,
                remainingDigits.substring(1),
                currentPath + letter
            );
        }

    }
}
```
```
**Time Complexity:**  O(3^M * 4^N)

**Space Complexity:**  O(3^M * 4^N)

Where:  
- M: number of digits mapping to 3 letters  
- N: number of digits mapping to 4 letters  
```


```text
Input: "29"

1. initial call: backtrack(phone, combinations, "29", "")
   currentDigit = '2' → letters = "abc"

2. loop over letters in "abc"

   ├─ letter = 'a'
   │   └─ backtrack(phone, combinations, "9", "a")
   │       currentDigit = '9' → letters = "wxyz"
   │
   │       ├─ letter = 'w'
   │       │   └─ backtrack(phone, combinations, "", "aw")
   │       │       remainingDigits is empty → combinations = ["aw"]
   │       │
   │       ├─ letter = 'x'
   │       │   └─ backtrack(phone, combinations, "", "ax")
   │       │       → combinations = ["aw", "ax"]
   │       │
   │       ├─ letter = 'y'
   │       │   └─ backtrack(phone, combinations, "", "ay")
   │       │       → combinations = ["aw", "ax", "ay"]
   │       │
   │       └─ letter = 'z'
   │           └─ backtrack(phone, combinations, "", "az")
   │               → combinations = ["aw", "ax", "ay", "az"]

   ├─ letter = 'b'
   │   └─ backtrack(phone, combinations, "9", "b")
   │       currentDigit = '9' → letters = "wxyz"
   │
   │       ├─ backtrack("", "bw") → combinations = [..., "bw"]
   │       ├─ backtrack("", "bx") → combinations = [..., "bx"]
   │       ├─ backtrack("", "by") → combinations = [..., "by"]
   │       └─ backtrack("", "bz") → combinations = [..., "bz"]

   └─ letter = 'c'
       └─ backtrack(phone, combinations, "9", "c")
           currentDigit = '9' → letters = "wxyz"
           ├─ backtrack("", "cw") → combinations = [..., "cw"]
           ├─ backtrack("", "cx") → combinations = [..., "cx"]
           ├─ backtrack("", "cy") → combinations = [..., "cy"]
           └─ backtrack("", "cz") → combinations = [..., "cz"]
```