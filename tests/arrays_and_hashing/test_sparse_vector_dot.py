"""Unit test suite for Sparse Vector Dot Product."""
from src.arrays_and_hashing.sparse_vector_dot import SparseVectorDotProduct

def test_sparse_vector_dot_basic():
    solver = SparseVectorDotProduct()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_sparse_vector_dot_repeated():
    solver = SparseVectorDotProduct()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
