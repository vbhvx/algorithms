"""
Unit tests for Refill Water Plants Capacity Priority Queue
"""
from algorithms.practice.heaps_and_priority.refill_water_bottles import solve_refill_water_bottles

def test_refill_water_bottles_base():
    assert solve_refill_water_bottles() is True
    assert solve_refill_water_bottles([3, 1, 2]) == [1, 2, 3]

def test_refill_water_bottles_edge_cases():
    assert solve_refill_water_bottles("") == ""
    assert solve_refill_water_bottles(0) is True
    assert solve_refill_water_bottles(-5) is False
