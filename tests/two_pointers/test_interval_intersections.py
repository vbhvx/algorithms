"""Unit test suite for Interval List Intersections."""
from src.two_pointers.interval_intersections import IntervalListIntersections

def test_interval_intersections_basic():
    solver = IntervalListIntersections()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_interval_intersections_repeated():
    solver = IntervalListIntersections()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
