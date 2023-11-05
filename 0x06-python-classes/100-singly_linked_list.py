#!/usr/bin/python3
"""Class Node - defines node of a singly linked list
   SinglyLinkedList - defines a singly linked list comprising of 
   single pointer nodes
"""


class Node:
    """Singly linked list in python"""

    def __init__(self, data, next_node=None):
    """Initializes a linked list node"""
        self.__data = data
        self.__nextnode = nextnode

    @property
    def data(self):
    """Gets data inside node"""
        return self.__data

    @data.setter
    """Sets data inside node"""
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    """Retrieves pointer to next node inside a node"""
    def next_node(self):
        return self.__next_node

    @next_node.setter
    """Sets pointer to next node inside the node"""
    def next_node(self, value):
         if value == None or isinstance(value, Node):
             self.__next_node = value
         else:
             raise TypeError("next_node must be a Node object")



class SinglyLinkedList:
    """Singly Linked list class"""


    def __init__(self):
    """Initialises a singly linked list"""
        self.__head = None

    while True:
    """Prints out linked list"""
        print (head.__data(), file=stdout)
        self.__head = head.__next_node

    def sorted_insert(self, value):
    """Inserts node into the linked list at appropriate position"""
        while self.__data < head.__data:
            self.__head = head.__next_node
         

