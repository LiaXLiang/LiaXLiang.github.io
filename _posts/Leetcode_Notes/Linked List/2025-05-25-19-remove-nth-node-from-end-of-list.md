---
title: 19. Remove Nth Node From End of List
date: 2025-05-25
categories: [Leetcode_Notes, Linked List]
---

### **Intuition: The Ruler Metaphor**
Think of a ruler of fixed length n, where:
- The left endpoint starts at the head of the list.
- The right endpoint is at the n-th node from the head.

Now slide this ruler one node at a time toward the right until the right endpoint reaches the end of the list. 

At that moment: The left endpoint is exactly at the (length - n)-th node — that is, the node just before the one we need to remove.

This is the essence of the two-pointer approach, where:

- One pointer (fast) is advanced n steps ahead of the other (slow).
- Then both pointers move forward in lockstep.
- When fast reaches the end, slow is just before the target.

###  The Edge Case: Removing the Head Node
Now comes a subtle point:
If n == length of list, then the node to be removed is the head itself. This causes a problem: The node before the one we want to delete doesn’t exist.
Without access to the previous node, we can't reassign .next to skip the target.

=> We can use a simple but powerful trick: introduce a dummy (sentinel) node at the start of the list.

### Solution
```java
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode fast = dummy, slow = dummy;

        for(int i = 0; i < n; i++){
            fast = fast.next;
        }
        // Move both pointers until 'fast' reaches the end of the list
        while(fast.next != null){
            fast = fast.next;
            slow= slow.next;
        }

        slow.next = slow.next.next;
        /*
        Important: returning 'head' here would fail 
        when the original head is removed
        */
        return dummy.next; 
    }
}
```
### Should I use ```while (node)``` or ```while (node.next)``` in my loop?
- (1) ```while (node)```
   - **while (node)** checks if ***the current node exists***. It raverse all nodes, including the last node
   - e.g. Printing All Node Values
   ```java
    while (node != null) {
        System.out.println(node.val);
        node = node.next;
    }
    ```
    We need to print every value, including the last node. So node must reach the end and process the node whose next == null.
- (2) ```while (node.next)``` 
  - **while (node.next)** checks if ***there is a next node available***, which is useful if you plan to access or modify node.next. It traverse up to the node before a target node
  - e.g. Deleting the Next Node
  ```java
  while (node.next != null) {

    if (node.next.val == target) {
        node.next = node.next.next;
    } else {
        node = node.next;
    }

  }
  ```
  Here we must stop **at the node before** the one we want to remove, so we can safely access and reassign node.next.

### Why should I return dummy.next instead of head when using a dummy (sentinel) node?
The key lies in understanding what *head* and *dummy* represent, and how modifying the list (especially when deleting the head node) affects them.
```java
ListNode dummy = new ListNode(0, head);  
// dummy.next = head
```
- *head* is a reference to the original head node.
- *dummy* is a new node that points to head, acting as a fixed, external anchor.

If the first node (i.e., the original head) gets deleted, *head* still points to the now-deleted node, and returning it is incorrect. However, *dummy.next* always reflects the updated head of the modified list.

