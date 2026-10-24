"""
Unit tests for Dota2 Senate Round-Robin Queue Elimination
"""
from algorithms.practice.greedy_algorithms.dota2_senate_queue import solve_dota2_senate_queue

def test_dota2_senate_queue_base():
    assert solve_dota2_senate_queue() is True
    assert solve_dota2_senate_queue([3, 1, 2]) == [1, 2, 3]

def test_dota2_senate_queue_edge_cases():
    assert solve_dota2_senate_queue("") == ""
    assert solve_dota2_senate_queue(0) is True
    assert solve_dota2_senate_queue(-5) is False
