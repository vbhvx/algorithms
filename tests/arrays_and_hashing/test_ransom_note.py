"""Unit test suite for Ransom Note Frequency Match."""
from src.arrays_and_hashing.ransom_note import RansomNoteFrequencyMatch

def test_ransom_note_basic():
    solver = RansomNoteFrequencyMatch()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_ransom_note_repeated():
    solver = RansomNoteFrequencyMatch()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
