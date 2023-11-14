#!/usr/bin/python3
"""Class Node - defines node of a singly linked list
   SinglyLinkedList - defines a singly linked list comprising of 
   single pointer nodes
"""


class Node:
    """Node implementation in python"""

    def __init__(self, data, next_node=None):
        """Initializes a linked list node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets data inside node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets data inside node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieves pointer to next node inside a node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
         """Sets pointer to next node inside the node"""
         if value == None or isinstance(value, Node):
             self.__next_node = value
         else:
             raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """Singly Linked list class"""

    def __init__(self):
        """Initialises a singly linked list"""
        self.__head = None

    def __str__(self):
        """Prints out linked list"""
        my_list = []
        itertr = self.__head
        while itertr is not None:
            my_list.append(itertr.data)
            itertr = itertr.next_node
        my_list.sort()
        finale = '\n'.join(str(elm) for elm in my_list)
        return finale

    def sorted_insert(self, value):
        """Inserts node into the linked list at appropriate position"""
        if self.__head is None:
            self.__head = Node(value, self.__head)
            return
        new_node = Node(value, self.__head)
        self.__head = new_node
