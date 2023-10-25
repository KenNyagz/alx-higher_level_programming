#!/usr/bin/pyhton3
"""Class Node - defines node of a singly linked list"""


class Node:
    """Singly linked list in python"""

    def __init__(self, value):
        self.__data = data

    def __init__(self, value):
        self.__next_node = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
         if value == None or isinstance(value, Node):
             self.__next_node = value
         else:
             raise TypeError("next_node must be a Node object")

     def __init__(self, data, next_node=None):
         self.__data = data
         self.__next_node = next_node


class SinglyLinkedList:
    """Singly Linked list class"""


    def __init__(self):
        self.__head = None

    while True:
        print (head.__data(), file=stdout)
        self.__head = head.__next_node

     def sorted_insert(self, value):
         while self.__data < head.__data:
             self.__head = head.__next_node
         
         self.__data = valxue




