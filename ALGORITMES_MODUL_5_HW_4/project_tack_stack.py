import datetime
#import datetime
from datetime import datetime
class ProjectTask:
    def __init__(self, description: str, duedate: datetime):
        self.descpription = description
        self.duedate = str(duedate)

    def __repr__(self):
        return f'{self.descpription, self.duedate}'


class Node:
    def __init__(self, data=ProjectTask):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, elem):
        node = Node(elem)
        if self.top:
            node.next = self.top
        self.top = node
        self.count += 1

    def pop(self):
        if not self.top:
            return None
        elem = self.top.data
        self.top = self.top.next
        self.count -= 1
        return elem

    def peek(self):
        if not self.top:
            return None
        return self.top.data

    def is_empty(self):
        return self.top == None

    def count(self):
        return self.count

p=ProjectTask('орать',datetime(2025,12,30))
p1=ProjectTask('бухать',datetime(2025,12,31))
p2=ProjectTask('опохмеляться',datetime(2026,1,1))
e=Stack()
e.push(p)
print(e.peek())
e.push(p1)
e.push(p2)
print(e.peek())
print(e.pop())
print(e.peek())

