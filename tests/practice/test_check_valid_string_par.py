"""
Unit tests for Valid Parenthesis String Wildcards
"""
from algorithms.practice.stack_and_queue.check_valid_string_par import solve_check_valid_string_par

def test_check_valid_string_par_base():
    assert solve_check_valid_string_par() is True
    assert solve_check_valid_string_par([3, 1, 2]) == [1, 2, 3]

def test_check_valid_string_par_edge_cases():
    assert solve_check_valid_string_par("") == ""
    assert solve_check_valid_string_par(0) is True
    assert solve_check_valid_string_par(-5) is False
