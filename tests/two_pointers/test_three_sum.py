"""Unit test suite for 3Sum Zero Triplet Two Pointers."""
from src.two_pointers.three_sum import 3SumZeroTripletTwoPointers

def test_three_sum_basic():
    solver = 3SumZeroTripletTwoPointers()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_three_sum_repeated():
    solver = 3SumZeroTripletTwoPointers()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
