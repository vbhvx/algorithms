"""
Unit tests for Sparse Vector Dot Product
"""
from algorithms.practice.arrays_and_hashing.sparse_vector_dot import solve_sparse_vector_dot

def test_sparse_vector_dot_base():
    assert solve_sparse_vector_dot() is True
    assert solve_sparse_vector_dot([3, 1, 2]) == [1, 2, 3]

def test_sparse_vector_dot_edge_cases():
    assert solve_sparse_vector_dot("") == ""
    assert solve_sparse_vector_dot(0) is True
    assert solve_sparse_vector_dot(-5) is False
