
class PersonCard:
    def __init__(self, name: str, age: int, occupation: str):
        self.name = name
        self.age = age
        self.occupation = occupation

    def __repr__(self):
        return f'{self.name, self.age, self.occupation}'

class Node:
    def __init__(self, data=PersonCard):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def add_person(self, data): # ! вставка карточки персоны в начало списка
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def append_person(self, item): # ! вставка карточки персоны в конец списка
        node = Node(item)

        if self.head is None:
            self.head = node
            return None

        iter = self.head
        while iter.next is not None:
            iter = iter.next

        iter.next = node
        self.count += 1


    def insert_person_at(self, index, data): # ! Вставляет новую карточку персоны person на позицию с указанным индексом
        if index < 0 or index > self.count: raise ValueError('Значение индекса не входит в параметры длины списка !')
        if index == 0: self.add_person(data)
        else:
            i = 0
            n = self.head
            while i+1 < index and n is not None:
                n = n.next
                i += 1
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
            self.count += 1

    def remove_first_person(self):  # ! удаляет первую карточку в списке и возвращает ее
        if not self.head:
            return None
        elem = self.head.data
        self.head = self.head.next
        self.count -= 1
        return elem

    def remove_last_person(self): # ! удаляет последнюю карточку в списке и возвращает ее
        temp = self.head
        prev = None
        while temp.next is not None:
            prev = temp
            temp = temp.next
        next_elem = prev.next
        prev.next = None
        self.count -= 1
        return next_elem

    def remove_person(self, elem): # ! удаляет карточку персоны, соответствующей переданной
        current = self.head

        if current and current.data == elem:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != elem:
            prev = current
            current = current.next
        self.count -= 1
        if not current:
            return None
        else:
            prev.next = current.next
            current = None


    def print_all_elem(self): # ! выводит все элементы односвязного списка
        current = self.head
        while current:
            print(current.data)
            current = current.next


    def contains(self, data): # ! показывает все карточки списка
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


    def total_people(self): # ! возвращает кол_во карточек в списке
        return self.count


    def is_empty(self): # ! возвращает True, если список пуст. Иначе - False
        return self.total_people() != 0


    def clear_all(self): # ! очищает список, удаляя все карточки
        self.head = None


