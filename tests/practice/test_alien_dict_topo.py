"""
Unit tests for Alien Dictionary Topological Sort Shortest Path
"""
from algorithms.practice.shortest_paths.alien_dict_topo import solve_alien_dict_topo

def test_alien_dict_topo_base():
    assert solve_alien_dict_topo() is True
    assert solve_alien_dict_topo([3, 1, 2]) == [1, 2, 3]

def test_alien_dict_topo_edge_cases():
    assert solve_alien_dict_topo("") == ""
    assert solve_alien_dict_topo(0) is True
    assert solve_alien_dict_topo(-5) is False
