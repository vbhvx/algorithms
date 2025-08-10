from algorithms.graphs.traversals import bfs_traversal, dfs_traversal

def test_traversals():
    adj = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    assert bfs_traversal(adj, 2) == [2, 0, 3, 1]
    assert dfs_traversal(adj, 2) == [2, 0, 1, 3]
