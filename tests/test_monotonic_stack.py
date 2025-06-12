from data_structures.monotonic_stack import next_greater_elements

def test_monotonic_stack():
    arr = [2, 1, 2, 4, 3]
    assert next_greater_elements(arr) == [4, 2, 4, -1, -1]
