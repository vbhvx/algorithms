"""
Unit tests for Word Ladder Shortest Transformation BFS
"""
from algorithms.practice.graphs_and_traversals.word_ladder_bfs import solve_word_ladder_bfs

def test_word_ladder_bfs_base():
    assert solve_word_ladder_bfs() is True
    assert solve_word_ladder_bfs([3, 1, 2]) == [1, 2, 3]

def test_word_ladder_bfs_edge_cases():
    assert solve_word_ladder_bfs("") == ""
    assert solve_word_ladder_bfs(0) is True
    assert solve_word_ladder_bfs(-5) is False
