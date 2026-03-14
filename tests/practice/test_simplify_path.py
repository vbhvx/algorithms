"""
Unit tests for Simplify Path Canonical UNIX Stack
"""
from algorithms.practice.stack_and_queue.simplify_path import solve_simplify_path

def test_simplify_path_base():
    assert solve_simplify_path() is True
    assert solve_simplify_path([3, 1, 2]) == [1, 2, 3]

def test_simplify_path_edge_cases():
    assert solve_simplify_path("") == ""
    assert solve_simplify_path(0) is True
    assert solve_simplify_path(-5) is False
