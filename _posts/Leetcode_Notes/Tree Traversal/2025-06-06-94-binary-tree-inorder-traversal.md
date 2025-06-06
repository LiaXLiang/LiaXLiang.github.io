---
title: 94 Binary Tree Inorder Traversal
date: 2025-06-06
categories: [Leetcode_Notes, Tree Traversal]
---

# I. Recursive Approach
### Algorithm Logic
1. **Define the function signature**
   
   Inorder traversal is a process, and the traversal result must be built as the recursion unfolds. So we need a place to accumulate results. To achieve this, we define a helper function that takes two parameters:
   - The current node being visited
   - A list that accumulates the traversal output in correct order
2. **Define the base case (termination condition)**
   
   If the current node is null, it means we've reached a leaf node’s child — this is valid by default, so return true.
3. **Define the recursive logic**
   
   For each non-null node: 
   - Recursively traverse the **left subtree**.
   - Add the current node's value into the result.
   - Recursively validate the **right subtree**. 

### Solution
```java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        inorderTraversal(root, res);
        return res;
    }
    private void inorderTraversal(TreeNode node, List<Integer> res){
        if(node == null) return;

        inorderTraversal(node.left, res);
        res.add(node.val);
        inorderTraversal(node.right, res);
    }
}
```



# II. Iterative Approach
Recursion is elegant and expressive, but in the case of very deep or highly skewed trees (e.g., a long chain of left children), the recursion depth may exceed the **call stack** limit, resulting in a **StackOverflowError**. This happens because the **call stack** in most mainstream programming language environments has a limited capacity, typically around 1,000 to 10,000 frames. In contrast, an iterative approach using an explicit stack (such as a Deque) avoids this limitation and offers more control over the traversal process.

### Algorithm Logic
We need to simulate the call stack using an explicit stack data structure.
#### What does the call stack do in recursion?
It keeps track of nodes we're visiting but haven't processed yet (because we’re waiting to visit their left children first).

So, when we reach a node, we:
- Push it onto the stack
- Move to its left child (because inorder means "left first").
- When we reach the bottom (```null```), we backtrack (```pop```).
- Then visit the node (add its value).
- Then proceed to its right child.

### Solution
```java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        List<Integer> res = new ArrayList<>();

        while (root != null || !stack.isEmpty()) {
            while(root != null){
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            res.add(root.val); 
            root = root.right;  
        }
        return res;
    }
}
```
