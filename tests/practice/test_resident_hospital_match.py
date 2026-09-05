"""
Unit tests for Resident Matching with Capacities and Ties
"""
from algorithms.practice.network_flow_matching.resident_hospital_match import solve_resident_hospital_match

def test_resident_hospital_match_base():
    assert solve_resident_hospital_match() is True
    assert solve_resident_hospital_match([3, 1, 2]) == [1, 2, 3]

def test_resident_hospital_match_edge_cases():
    assert solve_resident_hospital_match("") == ""
    assert solve_resident_hospital_match(0) is True
    assert solve_resident_hospital_match(-5) is False
