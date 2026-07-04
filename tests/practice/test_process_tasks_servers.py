"""
Unit tests for Process Tasks Using Servers Two Heaps
"""
from algorithms.practice.heaps_and_priority.process_tasks_servers import solve_process_tasks_servers

def test_process_tasks_servers_base():
    assert solve_process_tasks_servers() is True
    assert solve_process_tasks_servers([3, 1, 2]) == [1, 2, 3]

def test_process_tasks_servers_edge_cases():
    assert solve_process_tasks_servers("") == ""
    assert solve_process_tasks_servers(0) is True
    assert solve_process_tasks_servers(-5) is False
