---
title: 2832. Maximal Range That Each Element Is Maximum in It
date: 2025-05-29
categories: 
  - Leetcode_Notes
  - Stack
  - Monotonic Stack
---

### Why Monotonic Stack?

When a problem involves identifying the nearest greater or smaller element to the left or right, that's a strong indicator that a monotonic stack should be used. In this particular task, we are asked to find the range in which each element is the maximum — a condition that naturally lends itself to the monotonic stack.

### Revisiting the Monotonic Stack with an Example

Let’s review what happens in a **monotonic increasing stack** scenario, where the elements are arranged in increasing order from top to bottom. We'll iterate through the array from right to left, because we’re trying to find for each element the nearest element greater than it on the right.

```java
nums = [5, 1, 6, 2, 4]
```
 - Step 1: Stack is empty → Push 4
    ```

    |     |
    |  4  |
    +-----+
    ```
- Step 2: 2 < 4 → Push 2
    ```

    |     |
    |  2  |
    |  4  |
    +-----+
    ```
- Step 3: 
  - (1) 6 > 2 → Pop 2  
    ```

    |     |
    |  4  |
    +-----+
    ```
  - (2) 6 > 4 → Pop 4      
    ```

    |     |
    +-----+
    ```
  - (3) Stack is now empty → Push 6
    ```

    |     |
    |  6  |
    +-----+
    ```
- Step 4: 1 < 6 → Push 1
    ```

    |     |
    |  1  |
    |  6  |
    +-----+
    ```
- Step 5: 
  - (1) 5 > 1 → Pop 1  
    ```

    |     |
    |  6  |
    +-----+
    ```
  - (2) 5 < 6 → Push 5
    ```
    
    |     |
    |  5  |
    |  6  |
    +-----+
    ```

### Push vs. Pop Operations — What's Really Happening?

#### I. Push Operations — When Do They Occur?

We push the ```current element``` in two scenarios:

1. **Stack is empty**
   - 1.1. At the very beginning.
     - (e.g., Step1 - push *4*)
   - 1.2. After popping all smaller elements 
     - (e.g., Step3 - push *6* after popping *2* and *4*).
     - In this case, we can confirm that there is no greater element then the ```current element``` to the right, so the ***right boundary*** of the ```current element``` is the end of the array (nums.length).
  
   - Note that 1.1 can be thought of as a special case of 1.2 — imagine there's an infinitely small element at the bottom of the stack.
2. **Stack is not empty, and ```current element``` < ```stack top```**
   - (e.g. Step 2:  2 < 4 → Push 2)
  
   - Here, the stack bottom becomes the ***right boundary*** of the current element. The ```current element``` is waiting for its left boundary to be discovered later, but its ***right boundary*** is already clear.


#### II. Pop Operations — When Do They Occur?

We only pop from the stack when the **```current element``` > ```stack top```**.
- (e.g., Step 3(1): 6 > 2 → Pop 2) 
  - When we pop 2: 
    - Right boundary: index of 4 (the next larger on the right)
    - Left boundary: index of 6 (the next larger on the left — ```current element```)
- This pop action gives us both boundaries.
  - The ```current element``` is the first greater element on the left.
  - The next element in the stack **after pop** is the first greater element on the right.

### Final Stack — After All Elements Are Processed
Now consider an ascending input:
```java
nums = [1, 2, 3, 4, 5]
``` 
After the full iteration, some elements may still remain in the stack.

This occurs when no greater element appeared to the right of these elements — hence, they were never popped. As a result:
- Their right boundary is just themselves.
- Their left boundary can be determined by the element currently above them in the stack.

Finally, if there's only one element left in the stack during post-processing, that means it's the maximum element in the array. It has no greater element on either side.

### Why Store Indices Instead of Values?
To determine both left and right bounds, we need to know the position of each element. That's why we store indices, not just values.

### Solution
```java
class Solution {
    public int[] maximumLengthOfRanges(int[] nums) {
        Stack<Integer> s = new Stack<>();
        int n = nums.length;
        
        // Scan from right to left to process the right boundaries
        for (int i = n - 1; i >= 0; i--) {
            // If the current element is greater than the top of the stack,
            // we can determine the boundary for the element at the top
            while (!s.isEmpty() && nums[i] > nums[s.peek()]) {
                int cur = s.pop();
                nums[cur] = s.isEmpty() ? n - i - 1 : s.peek() - i - 1;
            }
            s.push(i);
        }

        // Process the remaining elements in the stack to calculate their left boundaries
        int left = s.peek();
        while (!s.isEmpty()) {
            int cur = s.pop();
            nums[cur] = s.isEmpty() ? n : s.peek() - left;
        }
        
        return nums;
    }
}
```

```
Time Complexity: O(N)
- First for loop: O(N)
  Each element is pushed to the stack once and popped at most once.
- Second while (!s.isEmpty()) loop: O(N)
  Processes the remaining elements in the stack. Each element is popped once, which also takes O(n) in total.

Space Complexity: O(N)
- The algorithm uses a stack Stack<Integer> s to store indices. In the worst case (e.g., a strictly decreasing array), all elements could be pushed onto the stack.
```