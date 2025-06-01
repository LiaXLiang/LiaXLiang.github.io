---
title: 997 Find the Town Judge
date: 2025-05-28
categories: [Leetcode_Notes, Word Problem]
---

### 📌 Algorithm
To efficiently determine who the judge is (if any), we assign each person a trust-score using an array trustScore of size *n + 1*. We use *n + 1* so that we can conveniently map person i to ```trustScore[i]```, avoiding off-by-one index confusion.

We then iterate over the trust array:
```java
for (int[] t : trust) {
    int a = t[0]; // person who trusts
    int b = t[1]; // person who is trusted

    // a trusts someone, so can't be the judge. His score decreases
    trustScore[a]--; 
    // b is trusted, so possibly the judge. His score increases
    trustScore[b]++; 
}
```
In the end, the town judge must have a trust score of exactly n - 1, meaning he is trusted by everyone else and trust no one.

After processing all trust relationships, we scan the array to find the one and only person with a trust score of n - 1.

### Solution
```java
class Solution {
    public int findJudge(int n, int[][] trust) {

        // Not enough trust relationships for a judge to exist
        if(trust.length < n - 1) return -1;

        // One person with no trust → is the judge
        if(n == 1 && trust.length == 0) return 1; 

        int[] trustScore = new int[n + 1];

        for (int[] relation : trust) {
            int a_i = relation[0];
            int b_i = relation[1];
            trustScore[a_i]--; //Cannot be judge
            trustScore[b_i]++; // Potential judge
        }
        
        int count = 0;
        int judge = 0;
        for(int i = 0; i < n + 1; i++){
            if(trustScore[i] == n - 1){
                count++;
                judge = i;
            }
        }
        return (count == 1) ? judge : -1;
        
    }
}
```

```
Time Complexity: O(T + N) 
T is the length of the trust array and N is the number of people.

Space Complexity: O(N)
for the trust score array.
```
