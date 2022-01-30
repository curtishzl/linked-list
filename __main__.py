
from linked_list import Node, LinkedList

def main():
    l1 = LinkedList()
    l1.add(2)
    l1.add(3)

    l2 = LinkedList()
    l2.add(2)
    l2.add(3)

    print(l1 == l2)


def print_list(lis):
    print(str(lis) + '\t head: ' + str(lis.head) + "\t tail: " + str(lis.tail) + "\t length: " + str(lis.length))


if __name__ == '__main__':
    main()