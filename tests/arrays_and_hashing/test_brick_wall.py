"""Unit test suite for Brick Wall Minimum Cross Cuts."""
from src.arrays_and_hashing.brick_wall import BrickWallMinimumCrossCuts

def test_brick_wall_basic():
    solver = BrickWallMinimumCrossCuts()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_brick_wall_repeated():
    solver = BrickWallMinimumCrossCuts()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
