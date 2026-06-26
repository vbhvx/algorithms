"""
Unit tests for Task Scheduler MaxHeap Frequency Math
"""
from algorithms.practice.heaps_and_priority.task_scheduler import solve_task_scheduler

def test_task_scheduler_base():
    assert solve_task_scheduler() is True
    assert solve_task_scheduler([3, 1, 2]) == [1, 2, 3]

def test_task_scheduler_edge_cases():
    assert solve_task_scheduler("") == ""
    assert solve_task_scheduler(0) is True
    assert solve_task_scheduler(-5) is False
