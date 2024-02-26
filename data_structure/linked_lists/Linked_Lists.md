
# Linked Lists

Linked lists are linear collections of independent nodes that are linked together via address pointers. Each linked-list is comprised of a header node, n-number data nodes, and a tail node, which is simply the last node in the linked-list and points to a null value. 

**[head]** -> **[data]** -> **[data]** -> **[data]** -> null  

---

### Basic forms of linked-lists: Singly and Doubly-linked

The most basic form of linked list is called a singly-linked list. Each node in a singly-linked list has two fields, the data field and the next element pointer.  

**[ data | nxt.ptr ]**  

This allows us to traverse linearly, starting at the head node, and access the different nodes within the linked list in order.

The next iteration of the linked-list is called the doubly-linked list, which adds a previous pointer field to the nodes.  

**[ prev.ptr | data | nxt.ptr ]**  

While we still have to traverse linearly, it allows us to move forward and backwards between nodes. It also makes the tail node more important.

---
### Tail Nodes

In a singly-linked list, the tail-node is an abstracted construct that just means we are at the end of the linked list. But since all nodes in a doubly-linked list have pointers to the previous node, we are now able to traverse the linked-list starting at the tail.

---

### Sentinel Nodes

Sentinel nodes, also called dummy nodes, are empty nodes that are used for the header node and/or tail node and act as the traversal path orginator (header sentinel node) and terminator (tail sentinel node).