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

    def __init__(self):
        # Creates a head node without any data
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        # Starts at the head, the left most point
        cur = self.head
        # Iterates through the list to the end, and adds in the new node
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        """
        
        """
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    def display(self):
        """
        Displays the contents of the singly-linked list

        Args:
            None

        Returns:
            None
        """
        contents = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            contents.append(cur.data)
        return contents

    def get(self, index):
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
     else:
        cur = self.head
        cur_idx = 0

        while True:
            last_node = cur
            cur = cur.next

            if cur_idx == index:
                last_node.next = cur.next
                return
            else:
                cur_idx += 1


if __name__ == "__main__":
    pass