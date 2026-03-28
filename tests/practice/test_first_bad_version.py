"""
Unit tests for First Bad Version Boundary Search
"""
from algorithms.practice.binary_search.first_bad_version import solve_first_bad_version

def test_first_bad_version_base():
    assert solve_first_bad_version() is True
    assert solve_first_bad_version([3, 1, 2]) == [1, 2, 3]

def test_first_bad_version_edge_cases():
    assert solve_first_bad_version("") == ""
    assert solve_first_bad_version(0) is True
    assert solve_first_bad_version(-5) is False
