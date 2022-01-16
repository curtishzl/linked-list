class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def add_first(self, node):
        if type(node) != Node:
            node = Node(node)

        if self.length == 0: # head and tail are None
            self.head = Node(node.value)
            self.tail = self.head

        elif self.length == 1: # head == tail
            node.next = self.head
            self.tail = self.head
            self.head = node

        else: # at least 2 nodes in list
            node.next = self.head
            self.head = node

        self.length += 1


    def add_last(self, node):
        if type(node) != Node:
            node = Node(node)

        if self.length == 0: # head and tail are None
            self.add_first(node)

        elif self.length == 1: # head == tail
            node.next = None
            self.head.next = node
            self.tail = node
            self.length += 1

        else: # at least 2 nodes in list
            node.next = None
            self.tail.next = node
            self.tail = node
            self.length += 1


    def add(self, node, index=None):
        if type(node) != Node:
            node = Node(node)

        if index == None:
            index = self.length # add to end by default
        elif index < 0 or index > self.length:
            raise IndexError('index ' + str(index) + ' out of bounds')
        
        if index == self.length: # includes length 0 and 1
            self.add_last(node)
        elif index == 0: # treat as special case because range(0-1) in the else block would not yield intended result
            self.add_first(node)
        else:
            node_i = self.head
            for i in range(index-1):
                node_i = node_i.next
            node.next = node_i.next
            node_i.next = node
            self.length += 1


    def remove_first(self):
        temp = self.head

        if self.length == 0:
            return temp
        elif self.length == 1:
            self.head = None
            self.tail = None
        elif self.length == 2:
            self.head = self.tail
            self.head.next = None
        else:
            self.head = self.head.next
        
        self.length -= 1
        return temp


    def remove_last(self):
        temp = self.tail

        if self.length == 0 or self.length == 1:
            return self.remove_first()
        elif self.length == 2:
            self.tail = self.head
            self.head.next = None
        else:
            node_i = self.head.next
            while node_i.next != self.tail: # traverse until the second to last node
                node_i = node_i.next
            node_i.next = None
            self.tail = node_i
        
        self.length -= 1
        return temp


    def remove(self, index=None):
        if index == None:
            index = self.length-1 # remove tail by default
        elif index < 0 or index >= self.length:
            raise IndexError('index ' + str(index) + ' out of bounds')

        if index == self.length-1: # includes 0 and 1
            return self.remove_last()
        elif index == 0:
            return self.remove_first()
        else:
            node_i = self.head
            for i in range(index-1):
                node_i = node_i.next
            temp = node_i.next
            node_i.next = node_i.next.next
            self.length -= 1
            return temp


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