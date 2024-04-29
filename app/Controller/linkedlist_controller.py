from Model import db_mysql
import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def clear(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def quickSort(self, data):
        if len(data) <= 1:
            return data
        else:
            pivot = data[0]

            less_than_pivot = [x for x in data[1:] if x <= pivot]
            greater_than_pivot = [x for x in data[1:] if x > pivot]

            return self.quickSort(less_than_pivot) + [pivot] + self.quickSort(greater_than_pivot)

    def jumpSearch(self, key, field):
        if not self.head:
            return None

        current = self.head
        while current:
            if current.data[field].lower() == key:
                return current.data
            current = current.next
        
        return None