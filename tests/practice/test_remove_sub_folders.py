"""
Unit tests for Remove Sub-Folders from Filesystem Trie
"""
from algorithms.practice.tries_and_prefix.remove_sub_folders import solve_remove_sub_folders

def test_remove_sub_folders_base():
    assert solve_remove_sub_folders() is True
    assert solve_remove_sub_folders([3, 1, 2]) == [1, 2, 3]

def test_remove_sub_folders_edge_cases():
    assert solve_remove_sub_folders("") == ""
    assert solve_remove_sub_folders(0) is True
    assert solve_remove_sub_folders(-5) is False
