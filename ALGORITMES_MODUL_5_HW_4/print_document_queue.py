
class PrintDocument:
    def __init__(self, title: str, number_of_pages: int):
        self.title = title
        self.number_of_pages = number_of_pages

    def __repr__(self):
        return f'{ self.title, self.number_of_pages}'

class Node:

    def __init__(self,prev, data=PrintDocument):
        self.prev = prev
        self.data = data




class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, item):
        node = Node(None, item)

        if self.is_empty():
            self.head = node
        else:
            self.tail.prev = node

        self.tail = node
        self.size += 1

    def dequeue(self):

        if self.is_empty():
            return None

        buff = self.head
        self.head = self.head.prev

        if self.head is None:
            self.tail = None

        self.size -= 1

        return buff.data


    def peek(self):
        if not self.is_empty():
            return self.head.data


    def count(self):
        return self.size

    def is_empty(self):
        return self.count() == 0