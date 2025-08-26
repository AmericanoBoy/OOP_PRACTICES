
from ALGORITMES_MODUL_5_HW_4 import print_document_queue

p = print_document_queue.PrintDocument('как заработать миллион', 1000)
p1 = print_document_queue.PrintDocument('как пробухать миллион', 10)
p2 = print_document_queue.PrintDocument('как выйти из запоя и снова заработать миллион', 10000)
p3 = print_document_queue.PrintDocument('как правильно повеситься, когда снова пропил миллион', 1)

def is_empty():
    q = print_document_queue.Queue()
    expected = True
    res = q.is_empty()
    assert expected == res, f'Ожидали:{expected}, получили:{res}'

def show_first_elem(p,p1,p2):
    q = print_document_queue.Queue()
    q.enqueue(p)
    q.enqueue(p1)
    q.enqueue(p2)
    expected = ('как заработать миллион', 1000)
    res = q.peek()
    assert expected == res, f'Ожидали:{expected}, получили:{res}'

def count(p):
    q = print_document_queue.Queue()
    q.enqueue(p)
    expected = 1
    res = q.count()
    assert expected == res, f'Ожидали:{expected}, получили:{res}'
