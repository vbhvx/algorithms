from data_structures.circular_queue import CircularQueue

def test_circular_queue():
    cq = CircularQueue(3)
    assert cq.enqueue(1) and cq.enqueue(2) and cq.enqueue(3)
    assert not cq.enqueue(4)
    assert cq.front() == 1
    cq.dequeue()
    assert cq.enqueue(4)
