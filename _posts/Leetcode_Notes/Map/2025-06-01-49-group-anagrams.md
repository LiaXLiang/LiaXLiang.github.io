---
title: 49 Group Anagrams
date: 2025-06-01
categories: [Leetcode_Notes, Map]
---

### Why HashMap?
When we see the problem - "**group the anagrams together**" - our immediate question is: "What does it mean for strings to be grouped together?"

That implies we need some way to **classify** or **categorize** strings that are *somehow equivalent*. Specifically, strings that are anagrams of each other should be placed into the same group.

But how do we check if two strings are anagrams? The trick is to **sort the characters in each string** - because anagrams have the same characters in different orders, sorting brings them to the same chanonical form.
- e.g. 
  - "eat" -> "aet"
  - "tea" -> "aet"
  - "tan" -> "ant"

Once we realized that sorted strings could serve as anagram signatures, the rest became clear: we need a way to map **each signature** to **a list of original strings** that share it.

HashMap naturally clicks:
- The key would be the sorted string (the anagram signature).
- The value would be a list of all strings that match that signature.


### Solution
```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        
        for(String str : strs){
            char[] array = str.toCharArray(); 
            Arrays.sort(array);               
            String key = new String(array);  
            if(map.containsKey(key)){
                map.get(key).add(str);
            }else{
                List<String> list = new ArrayList<>();
                list.add(str);
                map.put(key, list);
            }
        }
        return new ArrayList<List<String>>(map.values());
    }  
}
```
### Implementation Note
```java
if(map.containsKey(key)){
    map.get(key).add(str);
}else{
    List<String> list = new ArrayList<>();
    list.add(str);
    map.put(key, list);
}
```
can be simplified as 
```java
List<String> list = map.getOrDefault(key, new ArrayList<String>());
list.add(str);
map.put(key, list);
```

```
Time Complexity: O(Nklogk)
N := number of input strings in 'strs'
k := maximum length of a single string

For each input strings in 'strs':
    - converting to a char array: O(k)
    - sorting the array: O(klogk)
    - creating a string key: O(k)
    => Per string O(klogk)
Therefore, the total time complexity is O(n·klogk)

Space Complexity: O(Nk)
- HashMap storage: O(N)
    - HashMap stores up to N keys, each a string of length k.
- Temporary char arrays: O(k)
    - discarded after each iteration O(k) and not accumulatd.
- Sorted string keysL O(Nk)
    - Each key is a new string of length k, total n such keys.
```

