---
title: 17. Letter Combinations Of A Phone Number
date: 2025-05-15
categories: [Leetcode_Notes, BFS and DFS]
---

# I. BFS Queue-Based Approach

### Core Idea
We treat the process of building combinations as a breadth-first traversal: 
- Each digit adds a new "layer" of characters to all current strings.
- A queue helps track and generate combinations at each layer.
  
### 📌 Algorithm
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
      Step 0: Initialization

      Queue: [""]
      -----------------------------------------------------------

      Step 1: Process digit = '2' → letters = "abc"
      
      Initial queue size = 1
      Dequeue "" and append each letter in "abc": → "a", "b", "c"
      Updated Queue: ["a", "b", "c"]
      -----------------------------------------------------------

      Step 2: Process digit = '4' → letters = "ghi"
      Initial queue size = 3
      Dequeue each item and append every letter in "ghi":

      "a" → "ag", "ah", "ai"  
      "b" → "bg", "bh", "bi"  
      "c" → "cg", "ch", "ci"  

      Updated Queue:  
      ["ag", "ah", "ai", "bg", "bh", "bi", "cg", "ch", "ci"]
      -----------------------------------------------------------

      Step 3: Process digit = '9' → letters = "wxyz"
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
Time Complexity: O(3^M * 4^N)

Space Complexity:  O(3^M * 4^N)

Where:  
- M: number of digits mapping to 3 letters  
- N: number of digits mapping to 4 letters  
```

### Implementation Note 
#### Why capture the current queue size before expansion?
- This isolates processing to the existing combinations before expanding with the new digit's letters. It prevents mixing newly added items from the same round.

<br>
<br>  
<br>

# II. DFS Recursive Backtracking
### 💡 Backtracking Template
1. Backtracking is often used to explpore all possible configurations in a problem space. Conceptually, this can be modeled as a **tree traversal**, where:
   - Each **level** corresponds to a **step / input position** in the decision process, i.e., the recursion depth,
   - Each **node** respresents a **partial state** - a sequence of decisions made so far,
   - Each **branch** represents a **decision** made at a particular node,
   
   - A **leaf node** corresponds to a compete and valid result.
  
2. We can abstract the above *backtracking* process into 3 major components:
   - (***level*** is not explicitly tracked — recursion depth naturally encodes it.)
   - ```currentPath``` 
     - corresponds to the ***node*** in the tree model. 
     - Represents the current state — the sequence of decisions made from the root to the current node.
   - A **list of remaining choices / input**;
     - corresponds to the ***branch*** and implicitly to the ***level*** in the tree model, as each recursive call goes one level deeper. 
     - Defines which decisions can still be made from the current state — often used in a loop to explore all possible branches.
   - A **result list**
     - corresponds to the ***leaf node*** in the tree model.
     - Stores all complete and valid paths once the base case (leaf node) is reached.

4. Base Case (When to Terminate Recursion)
    - The base case is the condition that determines when a valid and complete solution has been reached. It is typically defined by:
      - A specific recursion depth,
      - An empty set of remaining input,
      - Or a problem-specific termination criterion.
    - Upon reaching the base case:
      - The current ```currentPath``` is added to resultList,
      - And the function returns without further recursion.

5. Decision-Making and Recursive Exploration (for-loop + recursive call)
    
    The core of backtracking follows a **decision + recursion + backtrack** pattern:
      - Iterate over all available choices at the current step (horizontal traversal).
      - For each choice:
        - Make a decision (append to ```currentPath```).
        - Recurse with updated parameters (descend vertically in the tree).
        - Undo the decision after recursion (backtrack), if using mutable structures like lists.
6. General Form of the Template
    ```java
    void backtrack(parameters...) {
        if (base case condition) {
            save result;
            return;
        }

        for (each choice in current level) {
            make decision;
            backtrack(next parameters); // go deeper (recursive call)
            undo decision if needed;   // backtrack (if using mutable structures)
        }
    }
    ```

***
Each recursive call peels off one digit and tries all corresponding letters.

- e.g.
    ```text
    Input: "29"

    1. initial call:
        backtrack("", phone, "29", combinations = [])
        currentDigit = '2' → letters = "abc"

    2. loop over letters in "abc"

    ├─ letter = 'a'
    │   └─ backtrack("a", phone, "9", combinations = [])
    │       currentDigit = '9' → letters = "wxyz"
    │
    │       ├─ letter = 'w'
    │       │   └─ backtrack("aw", phone, "", combinations = [])
    │       │       base case → combinations = ["aw"]
    │       │
    │       ├─ letter = 'x'
    │       │   └─ backtrack("ax", phone, "", combinations = ["aw"])
    │       │       base case → combinations = ["aw", "ax"]
    │       │
    │       ├─ letter = 'y'
    │       │   └─ backtrack("ay", phone, "", combinations = ["aw", "ax"])
    │       │       base case → combinations = ["aw", "ax", "ay"]
    │       │
    │       └─ letter = 'z'
    │           └─ backtrack("az", phone, "", combinations = ["aw", "ax", "ay"])
    │               base case → combinations = ["aw", "ax", "ay", "az"]
    
    ├─ letter = 'b'
    │   └─ backtrack("b", phone, "9", combinations = ["aw", "ax", "ay", "az"])
    │       currentDigit = '9' → letters = "wxyz"
    │
    │       ├─ backtrack("bw", phone, "", combinations = [...])
    │       │       base case → combinations = [..., "bw"]
    │       │
    │       ├─ backtrack("bx", phone, "", [..., "bw"])
    │       │       base case → combinations = [..., "bw", "bx"]
    │       │
    │       ├─ backtrack("by", phone, "", combinations = [..., "bw", "bx"])
    │       │       base case → combinations = [..., "bw", "bx", "by"]
    │       │
    │       └─ backtrack("bz", phone, "", combinations = [..., "bw", "bx", "by"])
   │       │       base case → combinations = [..., "bw", "bx", "by", "bz"]

    └─ letter = 'c'
        └─ backtrack("c", phone, "9", combinations)
            ├─ backtrack("cw", phone, "", combinations) → ...
            ├─ backtrack("cx", phone, "", combinations) → ...
            ├─ backtrack("cy", phone, "", combinations) → ...
            └─ backtrack("cz", phone, "", combinations) → ...
    ```

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
        backtrack("", phone, digits, combinations);
        return combinations;
    }

    public void backtrack(
        String currentPath,
        Map<Character, String> phone,
        String remainingDigits,
        List<String> combinations
    ) {
        if (remainingDigits.isEmpty()) {
            combinations.add(currentPath);
            return;
        }

        char currentDigit = remainingDigits.charAt(0);
        String letters = phone.get(currentDigit);

        for (char letter : letters.toCharArray()) {
            backtrack(
                currentPath + letter,
                phone,
                remainingDigits.substring(1),
                combinations
            );
        }
    }
}

```
```
Time Complexity: O(3^M * 4^N)
- M: number of digits mapping to 3 letters  
- N: number of digits mapping to 4 letters 

Space Complexity: O(3^M * 4^N)  
```


