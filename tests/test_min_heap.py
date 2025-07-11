from data_structures.min_heap import MinHeap

def test_min_heap():
    h = MinHeap()
    for x in [5, 3, 8, 1, 2]: h.push(x)
    res = [h.pop() for _ in range(5)]
    assert res == [1, 2, 3, 5, 8]
