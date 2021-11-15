class Node:
    """ An individual node, consists of data and a pointer to another node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """ A linked list. 'head' attribute is the beginning node of the list. """
    def __init__(self):
        self.head = None

    def add(self, data):
        """ Add a node to the beginning of the linked list. """
        node = Node(data)
        node.next = self.head
        self.head = node

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
