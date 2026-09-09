"""Unit test suite for 3Sum Closest Target Sum."""
from src.two_pointers.three_sum_closest import 3SumClosestTargetSum

def test_three_sum_closest_basic():
    solver = 3SumClosestTargetSum()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_three_sum_closest_repeated():
    solver = 3SumClosestTargetSum()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
