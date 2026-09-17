"""Unit test suite for 4Sum Quadruplet Two Pointers."""
from src.two_pointers.four_sum import 4SumQuadrupletTwoPointers

def test_four_sum_basic():
    solver = 4SumQuadrupletTwoPointers()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_four_sum_repeated():
    solver = 4SumQuadrupletTwoPointers()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
