class LinkedList:
    def __init__(self):
        pass

class Node:
    def __init__(self, val):
        self.__val = val
        self.__next = None

    @property
    def val(self):
        return self.__val

    @property
    def next(self):
        return self.__next

    @val.setter
    def val(self, val):
        self.__var = val

    @val.setter
    def next(self, next):
        if type(next) != Node:
            raise TypeError('must be of type Node')
        self.__next = next