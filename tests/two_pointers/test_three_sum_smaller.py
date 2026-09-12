"""Unit test suite for 3Sum Smaller Target Triplet Count."""
from src.two_pointers.three_sum_smaller import 3SumSmallerTargetTripletCount

def test_three_sum_smaller_basic():
    solver = 3SumSmallerTargetTripletCount()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_three_sum_smaller_repeated():
    solver = 3SumSmallerTargetTripletCount()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
