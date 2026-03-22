"""
Unit tests for Remove Duplicate Letters Lexicographical
"""
from algorithms.practice.stack_and_queue.remove_dup_letters import solve_remove_dup_letters

def test_remove_dup_letters_base():
    assert solve_remove_dup_letters() is True
    assert solve_remove_dup_letters([3, 1, 2]) == [1, 2, 3]

def test_remove_dup_letters_edge_cases():
    assert solve_remove_dup_letters("") == ""
    assert solve_remove_dup_letters(0) is True
    assert solve_remove_dup_letters(-5) is False
