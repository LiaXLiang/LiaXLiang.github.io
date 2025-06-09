---
title: 3 Longest Substring Without Repeating Characters
date: 2025-05-28
categories: [Leetcode_Notes, Two Pointers]
---
### A Ruler Metaphor
Imagine a ruler that can dynamically adjust its length. The goal is to position its left end (```start```) and right end (```cur```) over a substring such that all characters within the ruler's span are unique.

The right end (```cur```) moves forward one character at a time, scanning the string from left to right.

The left end (```start```) only advances when a duplicate character is found within the current window, ensuring all characters in the window remain distinct.


### 📌 Algorithm:
We use a hash map to record the last seen position of each character.

As we iterate through the string: 
- (1) For each character *c* at index ```cur```, we check:
  - Has this character been seen before?

- (2) If yes, was it seen **after or at** the start index? 
  
  —— If so, it means the character is inside the current substring window and violates the “no repetition” rule. In this case, we need to move the ```start``` to point to the position right after the last occurrence of that character.
    ```java 
    start = lastSeen.get(c) + 1; 
    ```
- (3) If the character has not been seen before, or was seen outside the current window, we don't need to move ```start```.
- (4) In both cases, we update the character's position in the map:
  ```java
  lastSeen.put(c, cur);
  ```
- (5) After that, compute the length of the current window:
  ```java
  int length = cur - start + 1;
  ```
  and then update the maximum length found so far.

### Solution
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> lastSeen = new HashMap<>();
        int start = 0, maxLen = 0;

        for (int cur = 0; cur < s.length(); cur++) {
            char c = s.charAt(cur);

            // If character was seen and is within the current window
            if (lastSeen.containsKey(c) && lastSeen.get(c) >= start) {
                // Move start right after the duplicate
                start = lastSeen.get(c) + 1; 
            }

            // Update character's latest position
            lastSeen.put(c, cur); 
            // Update max window length
            maxLen = Math.max(maxLen, cur - start + 1); 
        }

        return maxLen;
    }
}
```

```
Time Complexity: O(N)
N is the length of the string. In the worst case, both ends of the "ruler" (i.e., the start and current pointers of the sliding window) will each traverse the string once.

Space Complexity:  O(∣Σ∣)
Σ refers to the set of all possible characters that may appear in the string, and ∣Σ∣ represents the size of this set. Since the problem does not specify the character set explicitly, we can assume it to be the standard ASCII characters in the range [0, 128), so ∣Σ∣ = 128.
```