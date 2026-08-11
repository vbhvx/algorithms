"""
Unit tests for Accounts Merge Connected Components DSU
"""
from algorithms.practice.graphs_and_traversals.accounts_merge_graph import solve_accounts_merge_graph

def test_accounts_merge_graph_base():
    assert solve_accounts_merge_graph() is True
    assert solve_accounts_merge_graph([3, 1, 2]) == [1, 2, 3]

def test_accounts_merge_graph_edge_cases():
    assert solve_accounts_merge_graph("") == ""
    assert solve_accounts_merge_graph(0) is True
    assert solve_accounts_merge_graph(-5) is False
