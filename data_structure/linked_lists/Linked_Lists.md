
# Linked Lists

Linked lists are linear collections of independent nodes that are linked together via address pointers. Each linked-list is comprised of a header node, n-number data nodes, and a tail node. The header and tail nodes are the first and last nodes in the linked list respectively, and are either actual data nodes with values associated with them, or empty sentinel nodes. The header and tail nodes are important since they are the path traversal originator *(head node)* or terminator *(tail node)*.

**[head_data]** -> **[data]** -> **[tail_data]** -> null 

**[head_sentinel]** -> **[data]** -> **[data]** -> **[data]** -> **[tail_sentinel]** -> null  

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

In a singly-linked list, the tail node is simply the path traversal terminator. But since all nodes in a doubly-linked list have pointers to the previous node, we are now able to traverse the linked-list starting at the tail.

---

### Sentinel Nodes

Sentinel nodes, also called dummy nodes, are empty nodes that are used for the header node and/or tail node and act as the traversal path orginator (header sentinel node) and terminator (tail sentinel node).

---
---
---

### Other useful material
1. https://en.wikipedia.org/wiki/Linked_list  
2. https://en.wikipedia.org/wiki/Sentinel_node  
3. https://www.youtube.com/watch?v=_jQhALI4ujg
   - Good Computerphile video discussing linked-lists at a high level
4. https://builtin.com/data-science/python-linked-list
5. https://www.youtube.com/watch?v=JlMyYuY1aXU
   - Video tutorial of implementing singly-linked lists. This was what my implementation of singly-linked lists was initially based on. 
