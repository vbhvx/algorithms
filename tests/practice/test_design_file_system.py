"""
Unit tests for Design File System Trie Path Registry
"""
from algorithms.practice.tries_and_prefix.design_file_system import solve_design_file_system

def test_design_file_system_base():
    assert solve_design_file_system() is True
    assert solve_design_file_system([3, 1, 2]) == [1, 2, 3]

def test_design_file_system_edge_cases():
    assert solve_design_file_system("") == ""
    assert solve_design_file_system(0) is True
    assert solve_design_file_system(-5) is False
