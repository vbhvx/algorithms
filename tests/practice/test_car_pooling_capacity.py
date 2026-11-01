"""
Unit tests for Car Pooling Difference Array Capacity Sweep
"""
from algorithms.practice.intervals_scheduling.car_pooling_capacity import solve_car_pooling_capacity

def test_car_pooling_capacity_base():
    assert solve_car_pooling_capacity() is True
    assert solve_car_pooling_capacity([3, 1, 2]) == [1, 2, 3]

def test_car_pooling_capacity_edge_cases():
    assert solve_car_pooling_capacity("") == ""
    assert solve_car_pooling_capacity(0) is True
    assert solve_car_pooling_capacity(-5) is False
