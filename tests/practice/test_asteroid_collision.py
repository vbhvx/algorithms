"""
Unit tests for Asteroid Collision Stack Simulation
"""
from algorithms.practice.stack_and_queue.asteroid_collision import solve_asteroid_collision

def test_asteroid_collision_base():
    assert solve_asteroid_collision() is True
    assert solve_asteroid_collision([3, 1, 2]) == [1, 2, 3]

def test_asteroid_collision_edge_cases():
    assert solve_asteroid_collision("") == ""
    assert solve_asteroid_collision(0) is True
    assert solve_asteroid_collision(-5) is False
