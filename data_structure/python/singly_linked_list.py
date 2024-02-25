"""Module creating Singly-linked lists"""
class Node():
    """
    Basic Node class used in the LinkedList objects

    ...
    Atributes
    ---------
    data : int
        Integer value of node
    next : int
        Integer value of the next node
    """
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList():
    """
    Singly-linked list class that constructs and manipulates the list

    ...
    Atributes
    ---------
    head : None
        A blank node object to start the singly-linked list
    """

    def __init__(self, sentinel=True):
        self.sentinel = sentinel
        if sentinel is True:
            self.head = Node()
        else:
            self.head = None

    def insert(self, data, index=None):
        new_node = Node(data)
        # Establishes the new node as the head node in the case of there being no sentinal node
        if self.head is None:
            self.head = new_node
            return
        if index is None:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
        else:
            if index >= self.length():
                raise IndexError("Index is out of range")
            if index == 0:
                if self.head.data is None:
                    # Since the head node is a sentinel node, it contains no values and will be
                    # effectively removed from the linked list. As such, we need to maintain
                    # a pointer to the next node in the list.
                    next_pointer = self.head.next
                    self.head = new_node
                    self.head.next = next_pointer
                else:
                    # Since the old head node is not a sentinel node and will be retained,
                    # we will just be adding in a new node that points to the old head node.
                    # The old head node will retain its link to the next node in the list so
                    # the integrity of the linked list will be maintained.
                    temp_node = self.head
                    self.head = new_node
                    self.head.next = temp_node
            else:
                # The search begins at element 1 since there is specific logic for replacing
                # the head node. The node behind the current node needs to be tracked to link
                # it to the inserted node. An abstracted index counter, cur_idx, is used to
                # count and find the right value.
                prev = self.head
                cur = self.head.next
                cur_idx = 1
                while True:
                    if cur_idx == index:
                        temp_node = cur
                        cur = new_node
                        cur.next = temp_node
                        prev.next = cur
                        return
                    prev = prev.next
                    cur = cur.next
                    cur_idx += 1

    def length(self):
        """
        Displays the length of the singly-linked list.

        Starts at the head of the singly-linked list and traverses through the length of the nodes,
        adding one at each iteration to the 'total' variable. Stops and returns total when 
        cur.next equals None. 

        Args:
            None
        Returns:
            total(int) : total count of the nodes in the singly-linked list
        """

        # If there is no sentinel node, count the head node in the length of the linked-list.
        if self.sentinel is True:
            total = 0
        else:
            total = 1
        cur = self.head
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        """
        Displays the contents of the singly-linked list.

        Starts at the head of the singly-linked list and traverses through the length of the
        nodes, adding the contents of each node to a python list variable named 'contents' which
        is returned when cur.next equals None.

        Args:
            None
        Returns:
            contents(list) : A list of the contents of the singly-linked list
        """
        # The irony of using python's dynamic array implementation of a list to store and present
        # a singly-linked list is not lost on me.
        contents = []
        cur = self.head
        # Adds the head node to the contents list if there is no sentinel node
        if cur.data is not None:
            contents.append(cur.data)

        while cur.next is not None:
            cur = cur.next
            contents.append(cur.data)

        return contents

    def get_value(self, index):
        """
        Returns the value at the selected index.

        First checks the index value to validate if it is within the range of the singly-linked
        list object. Then starts at the head and instantiates an index counter variable, cur_idx,
        and adds to this counter for each node in the singly-linked list that is traversed. 
        Once the proper index is found, the value, cur.data, is returned.

        Technically, linked-lists are not indexed, so the counting variable, cur_idx, is used to
        abstract an index for the linked list.

        Args:
            index(int) : integer value representing the desired index
        Returns:
            cur.data(int) : the value of the node at the desired index
        """
        if index >= self.length():
            raise IndexError("Index out of range")
        cur = self.head
        cur_idx = 0
        # Advances the search in the list by one in case there is a sentinel node
        if self.head.data is None:
            while True:
                cur = cur.next
                if cur_idx == index:
                    return cur.data
                cur_idx += 1
        else:
            while True:
                if cur_idx == index:
                    return cur.data
                cur = cur.next
                cur_idx += 1
    def delete(self, index):
        if index >= self.length():
            raise IndexError("Index out of range")
        cur = self.head
        cur_idx = 0

        while True:
            last_node = cur
            cur = cur.next

            if cur_idx == index:
                last_node.next = cur.next
                return
            cur_idx += 1
