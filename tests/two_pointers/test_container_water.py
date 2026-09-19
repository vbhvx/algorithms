"""Unit test suite for Container With Most Water."""
from src.two_pointers.container_water import ContainerWithMostWater

def test_container_water_basic():
    solver = ContainerWithMostWater()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_container_water_repeated():
    solver = ContainerWithMostWater()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
