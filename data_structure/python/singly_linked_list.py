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

    def __init__(self):
        # Creates a head node without any data
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        # Starts at the head, the left most point
        cur = self.head
        # Iterates through the list to the end, and adds in the new node
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

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

        cur = self.head
        total = 0
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
        contents = []
        cur = self.head

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
        else:
            cur = self.head
            cur_idx = 0

            while True:
                cur = cur.next
                if cur_idx == index:
                    return cur.data
                else:
                    cur_idx += 1

    def erase(self, index):
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
