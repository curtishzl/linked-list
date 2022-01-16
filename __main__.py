
from linked_list import Node, LinkedList

def main():
    #print(LinkedList.___str__(Node('node')))
    lis = LinkedList()
    lis.add_last(Node(1))
    lis.add_first(Node(2))
    lis.add_last(Node(3))
    print(str(lis) + '\nhead: ' + str(lis.head) + "\ntail: " + str(lis.tail))

if __name__ == '__main__':
    main()