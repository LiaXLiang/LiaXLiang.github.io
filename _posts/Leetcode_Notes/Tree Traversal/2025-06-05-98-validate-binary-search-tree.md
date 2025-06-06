---
title: 98 Validate Binary Search Tree
date: 2025-06-05
categories: [Leetcode_Notes, Tree Traversal]
---

# I. Preorder Traversal 
# Root → Left → Right, validate before recursion
### A valid BST is defined as follows:
- The **left** subtree of a node contains only nodes with keys **less than** the node's key.
- The **right** subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.
  
Using this property, we can define a valid interval ```(lower, upper)``` for each node. 

For example, consider the node ④ in the tree below 
(the circled number represents both the node's value and its index in this discussion):

- It is the right child of node ②, so its value must be greater than 2.
- It is also in the left subtree of node ⑤, so its value must be less than 5.
- Therefore, the valid interval for node ④ is (2, 5).

For the root node, since there are no constraints from ancestors, we can assume an initial range of (−∞, ∞).
```
                      (−∞, ∞)
                         ⑤
                        /  \
                       /    \   
              (−∞, 5) ②     ⑥ (5, ∞)
                     /  \
                    /    \     
           (−∞, 2) ①     ④ (2, 5)
                         /
                        /
               (2, 4) ③
```
Note:
- Preorder Traversal: **[5,2,1,4,3,6]**
  - Root ⑤ 
  - Left subtree of 5: ② 
  - Left child of 2: ①
  - Right child of 2: ④
  - Left child of 4: ③
  - Right subtree of 5: ⑥
- Inorder Traversal: **[1,2,3,4,5,6]**
  - Leftmost node: ①
  - Back to node 2: ②
  - Left child of 4: ③
  - Node ④
  - Back to root ⑤
  - Right subtree: ⑥
- Post-order Traversal: **[1,3,4,2,6,5]**
  - Leftmost node: ①
  - Left subtree of 4: ③
  - Node ④
  - Node ②
  - Right subtree: ⑥
  - Root node: ⑤


### Algorithm Logic
1. **Define the function signature**
   
   To validate the BST, we define a recursive function with three parameters:
   - The current node being visited
   - Its lower bound ```left```
   - Its upper bound ```right```

2. **Define the base case (termination condition)**
   If the current node is null, it means we've reached a leaf node’s child — this is valid by default, so return true.
3. **Define the recursive logic**
   For each node: 
   - Check whether ```node.val``` lies strictly between ```left``` and ```right```
   - If it doesn’t, return false
   - If it does, recursively validate:
     - Left subtree:
       - Lower bound remains unchanged  
       - New *upper bound* is ```node.val```
       
     - Right subtree:
       - New *lower bound* is ```node.val```
       - *upper bound* remains unchanged  

### Solution
```java
class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean isValidBST(TreeNode node, long left, long right) {
        if (node == null) {
            return true;
        }

        long val = node.val;
        return left < val && val < right
            && isValidBST(node.left, left, val)
            && isValidBST(node.right, val, right);
    }
}
```

### Implementation Note
#### Why do we use ```long``` instead of ```int```?
Although all node values in the problem are of type *int*, we use *long* for the ```left``` and ```right``` boundaries in the recursion. Because at the very beginning, we need to assign the initial boundaries as wide as possible — strictly smaller and strictly greater than any possible *int* value. 

If we used ```Integer.MIN_VALUE``` and ```Integer.MAX_VALUE```, we would run into a problem: what if a node's value is exactly ```Integer.MIN_VALUE``` or ```Integer.MAX_VALUE```? The comparison ```val > left``` or ```val < right``` would fail since there would be no "smaller" or "larger" value to set as a strict bound using int.

Using int bounds would cause for example the test case ```[2147483647]```, where 2147483647 == ```Integer.MAX_VALUE``` to return false.

<br>
<br>  
<br>

# II. Inorder Traversal
# Left → Root → Right
Inorder traversal of a **BST** should produce **a strictly increasing sequence of values**.  This allows us to validate the BST property by simply checking whether each current node value is greater than the previous one.

### Algorithm Logic
1. **Define the function signature**
   
   We use a class-level variable ```pre``` to store the value of the previously visited node:
   - The current node being visited
   - The previous node's value
2. **Define the base case (termination condition)**
   
   If the current node is null, it means we've reached a leaf node’s child — this is valid by default, so return true.
3. **Define the recursive logic**
   
   For each node: 
   - Recursively validate the **left subtree**.
   - Check the current node's value:
     - If ```node.val <= pre```, it violates the BST property (should be strictly increasing), so return false.
     - Otherwise, update ```pre = node.val```
    - Recursively validate the **right subtree**. 


### Implementation Note
#### Class-level variable
The pre variable must be declared outside the recursive function, so its value is retained across the recursion calls.

### Solution
```java
class Solution {
    private long pre = Long.MIN_VALUE;

    public boolean isValidBST(TreeNode root) {
        if(root == null) return true;

        if(!isValidBST(root.left)) return false;

        if(root.val <= pre) return false;

        pre = root.val;
        return isValidBST(root.right);
    }
}
```


# III. Postorder Traversal