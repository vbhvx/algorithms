"""
Unit tests for Design Browser History DLL Simulation
"""
from algorithms.practice.linked_lists.design_browser_history import solve_design_browser_history

def test_design_browser_history_base():
    assert solve_design_browser_history() is True
    assert solve_design_browser_history([3, 1, 2]) == [1, 2, 3]

def test_design_browser_history_edge_cases():
    assert solve_design_browser_history("") == ""
    assert solve_design_browser_history(0) is True
    assert solve_design_browser_history(-5) is False
