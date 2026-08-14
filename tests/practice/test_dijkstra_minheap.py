"""
Unit tests for Dijkstra Shortest Path Adjacency MinHeap
"""
from algorithms.practice.shortest_paths.dijkstra_minheap import solve_dijkstra_minheap

def test_dijkstra_minheap_base():
    assert solve_dijkstra_minheap() is True
    assert solve_dijkstra_minheap([3, 1, 2]) == [1, 2, 3]

def test_dijkstra_minheap_edge_cases():
    assert solve_dijkstra_minheap("") == ""
    assert solve_dijkstra_minheap(0) is True
    assert solve_dijkstra_minheap(-5) is False
