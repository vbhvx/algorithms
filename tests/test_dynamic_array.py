from data_structures.dynamic_array import DynamicArray
import pytest

def test_dynamic_array():
    arr = DynamicArray(2)
    arr.append(10); arr.append(20); arr.append(30)
    assert arr.capacity == 4
    assert arr.size == 3
    assert arr.get(1) == 20
    assert arr.pop() == 30
