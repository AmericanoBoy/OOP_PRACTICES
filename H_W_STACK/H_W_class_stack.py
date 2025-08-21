
class Node: #класс узла
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack: #непосредственно сам класс стек
    def __init__(self):
        self.top = None #ссылка на узел в верхней части стека

    def push_elem(self, elem): #добавление нового узла в начало стека
        node = Node(elem)
        if self.top:
            node.next = self.top
        self.top = node

    def pop_elem(self): #удаление последнего элемента
        if not self.top:
            return None
        elem = self.top.data
        self.top = self.top.next
        return elem

    def peek_elem(self): #просмотр последнего элемента
        if not self.top:
            return None
        return self.top.data

    def is_empty(self): #проверка стека на наличие элементов
        return self.top == None
