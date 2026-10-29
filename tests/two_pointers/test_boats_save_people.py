"""Unit test suite for Boats to Save People Pairing."""
from src.two_pointers.boats_save_people import BoatsToSavePeoplePairing

def test_boats_save_people_basic():
    solver = BoatsToSavePeoplePairing()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_boats_save_people_repeated():
    solver = BoatsToSavePeoplePairing()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
