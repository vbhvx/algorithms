from data_structures.min_stack import MinStack

def test_min_stack():
    ms = MinStack()
    ms.push(5); ms.push(2); ms.push(10); ms.push(1)
    assert ms.get_min() == 1
    ms.pop()
    assert ms.get_min() == 2
