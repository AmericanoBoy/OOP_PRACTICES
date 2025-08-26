from datetime import datetime
from ALGORITMES_MODUL_5_HW_4 import project_tack_stack

p = project_tack_stack.ProjectTask('орать', datetime(2025, 12, 30))
p1 = project_tack_stack.ProjectTask('бухать', datetime(2025, 12, 31))
p2 = project_tack_stack.ProjectTask('опохмеляться', datetime(2026, 1, 1))

def is_empty():
    q = project_tack_stack.Stack()
    expected = True
    res = q.is_empty()
    assert expected == res, f'Ожидали:{expected}, получили:{res}'

def peek_elem(p,p1,p2):

    s = project_tack_stack.Stack()
    s.push(p)
    s.push(p1)
    s.push(p2)
    expected = ('опохмеляться', '2026-01-01 00:00:00')
    res = s.peek()
    assert expected == res, f'Ожидали:{expected}, получили:{res}'

def pop_elem(p,p1,p2):
    s = project_tack_stack.Stack()
    s.push(p)
    s.push(p1)
    s.push(p2)
    s.pop()
    s.pop()
    expected = ('бухать', '2025-12-31 00:00:00')
    res = s.peek()
    assert expected == res, f'Ожидали:{expected}, получили:{res}'

def count(p):
    s = project_tack_stack.Stack()
    s.push(p)
    expected = 1
    res = s.count()
    assert expected == res, f'Ожидали:{expected}, получили:{res}'


