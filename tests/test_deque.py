from data_structures.deque import Deque

def test_deque():
    d = Deque()
    d.push_back(10); d.push_front(5); d.push_back(20)
    assert d.pop_front() == 5
    assert d.pop_back() == 20
    assert d.pop_front() == 10
