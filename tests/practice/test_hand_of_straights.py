"""
Unit tests for Hand of Straights Consecutive Groups MinHeap
"""
from algorithms.practice.greedy_algorithms.hand_of_straights import solve_hand_of_straights

def test_hand_of_straights_base():
    assert solve_hand_of_straights() is True
    assert solve_hand_of_straights([3, 1, 2]) == [1, 2, 3]

def test_hand_of_straights_edge_cases():
    assert solve_hand_of_straights("") == ""
    assert solve_hand_of_straights(0) is True
    assert solve_hand_of_straights(-5) is False
