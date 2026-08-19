"""Unit test suite for Group Shifted Strings Canonical."""
from src.arrays_and_hashing.group_shifted_strings import GroupShiftedStringsCanonical

def test_group_shifted_strings_basic():
    solver = GroupShiftedStringsCanonical()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_group_shifted_strings_repeated():
    solver = GroupShiftedStringsCanonical()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
