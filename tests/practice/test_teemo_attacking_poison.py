"""
Unit tests for Teemo Attacking Non-Overlapping Duration
"""
from algorithms.practice.intervals_scheduling.teemo_attacking_poison import solve_teemo_attacking_poison

def test_teemo_attacking_poison_base():
    assert solve_teemo_attacking_poison() is True
    assert solve_teemo_attacking_poison([3, 1, 2]) == [1, 2, 3]

def test_teemo_attacking_poison_edge_cases():
    assert solve_teemo_attacking_poison("") == ""
    assert solve_teemo_attacking_poison(0) is True
    assert solve_teemo_attacking_poison(-5) is False
