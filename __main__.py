
from linked_list import Node, LinkedList

def main():
    #print(LinkedList.___str__(Node('node')))
    lis = LinkedList()
    lis.add(Node(1),0)
    lis.add(2)
    lis.add('xd')
    lis.add(Node(4),0)
    lis.add(Node(5))
    lis.add(Node(6),3)
    print(str(lis) + '\nhead: ' + str(lis.head) + "\ntail: " + str(lis.tail))

if __name__ == '__main__':
    main()