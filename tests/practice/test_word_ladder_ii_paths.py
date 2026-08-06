"""
Unit tests for Word Ladder II Bidirectional BFS Backtrack
"""
from algorithms.practice.graphs_and_traversals.word_ladder_ii_paths import solve_word_ladder_ii_paths

def test_word_ladder_ii_paths_base():
    assert solve_word_ladder_ii_paths() is True
    assert solve_word_ladder_ii_paths([3, 1, 2]) == [1, 2, 3]

def test_word_ladder_ii_paths_edge_cases():
    assert solve_word_ladder_ii_paths("") == ""
    assert solve_word_ladder_ii_paths(0) is True
    assert solve_word_ladder_ii_paths(-5) is False
