class Node:
    """ An individual node, consists of data and a pointer to another node. """
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    """ A linked list. 'head' attribute is the beginning node of the list. """
    def __init__(self):
        self.head = None
        self.tail = None

    def addToFront(self, data):
        """ Add a node to the beginning of the linked list. """
        node = Node(data)
        node.next = self.head

        if self.head is not None:
            self.head.prev = node
        else:
            self.tail = node # If the list is empty, both tail and head need to be the same.

        self.head = node

    def addToEnd(self, data):
        """ Add a node to the end of the linked list. """
        node = Node(data)
        node.prev = self.tail

        if self.tail is not None:
            self.tail.next = node
        else:
            self.head = node # If the list is empty, both head and tail need to be the same.

        self.tail = node

    def size(self):
        """ Return the size of the linked list. """
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next

        return count

    def isEmpty(self):
        if self.head is None:
            return True

        return False
    
    def print(self):
        """ Print the data from all of the list's nodes. """
        node = self.head
        while node is not None:
            print(node.data, " ", end="")
            node = node.next
        print()
