"""
Unit tests for Maximum Width Ramp Monotonic Index
"""
from algorithms.practice.stack_and_queue.max_width_ramp import solve_max_width_ramp

def test_max_width_ramp_base():
    assert solve_max_width_ramp() is True
    assert solve_max_width_ramp([3, 1, 2]) == [1, 2, 3]

def test_max_width_ramp_edge_cases():
    assert solve_max_width_ramp("") == ""
    assert solve_max_width_ramp(0) is True
    assert solve_max_width_ramp(-5) is False
