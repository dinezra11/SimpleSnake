class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while self.head.next is not None:
                node = node.next

            node.next = Node(data)

    def size(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next

        return count

    def print(self):
        node = self.head
        while node is not None:
            print(node.data, " ", end="")
            node = node.next
        print()
