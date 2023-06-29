#!/usr/bin/python3
"""module about linked list"""
class Node:
    @data.setter
    def data(self, data):
        """ function about data"""
        if type(self.__data) != int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def data(self):
        """ function about data"""
        return (self.__data)

    @property
    def next_node(self):
        """ function about data"""
        return self.__next

    @next_node.setter
    def next_node(self, n):
        """ function about data"""
        self.__next = n
        if self.__next != Node and self.__next != None:
            raise TypeError("next_node must be a Node object")

    def __init__(self, data, next_node=None):
        """ function about data"""
        self.__data = data
        self.__next = next_node


class SinglyLinkedList:
    def __init__(self):
        """ there is sth"""
        self.__head = None

    def sorted_insert(self, Value):
        """Insert a node."""
        n = Node(Value)
        if self.__head is None:
            self.__head = n
            return
        if Value < self.__head:
            self.__head = n
            return
        actual = self.__head
        while DataValue >= actual.data:
            prev = actual
            if actual.next_node:
                actual = actual.next_node
            else:
                actual.next_node = NewNode
                return
        prev.next_node = NewNode
        NewNode.next_node = actual

    def __str__(self):
        """one day Str"""
        strg = ""
        actual = self.__head
        while actual:
            strg += str(actual.data) + "\n"
            actual = actual.next_node
        return strg[:-1]
