"""Unit test suite for Move Zeroes In Place."""
from src.two_pointers.move_zeroes import MoveZeroesInPlace

def test_move_zeroes_basic():
    solver = MoveZeroesInPlace()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_move_zeroes_repeated():
    solver = MoveZeroesInPlace()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
