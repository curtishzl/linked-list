class LinkedList:
    def __init__(self, len=0):
        self.head = None
        self.tail = None

    def add_first(self, node):
        if self.len() == 0: # head and tail are None
            self.head = Node(node.value)
            self.tail = self.head

        elif self.len() == 1: # head == tail
            node.next = self.head
            self.tail = self.head
            self.head = node

        else: # at least 2 nodes in list
            node.next = self.head
            self.head = node

    def add_last(self, node):
        if self.len() == 0: # head and tail are None
            self.add_first(node)

        elif self.len() == 1: # head == tail
            node.next = None
            self.head.next = node
            self.tail = node

        else: # at least 2 nodes in list
            node.next = None
            self.tail.next = node
            self.tail = node
            


    def add(self, node, index):
        pass

    def len(self):
        len = 0
        node = self.head
        while node != None:
            len += 1
            node = node.next
        return len

    def __str__(self):
        node = self.head
        string = '['
        if node == None:
            return string + ']'

        while node != None:
            string += str(node) + ', '
            node = node.next
        return string[:-2] + ']'



class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)