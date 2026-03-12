"""
Unit tests for Car Fleet Monotonic Collision
"""
from algorithms.practice.stack_and_queue.car_fleet import solve_car_fleet

def test_car_fleet_base():
    assert solve_car_fleet() is True
    assert solve_car_fleet([3, 1, 2]) == [1, 2, 3]

def test_car_fleet_edge_cases():
    assert solve_car_fleet("") == ""
    assert solve_car_fleet(0) is True
    assert solve_car_fleet(-5) is False
