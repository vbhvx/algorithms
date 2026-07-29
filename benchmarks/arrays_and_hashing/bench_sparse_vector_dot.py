"""Benchmark profile for Sparse Vector Dot Product."""
import time
from src.arrays_and_hashing.sparse_vector_dot import SparseVectorDotProduct

def benchmark():
    solver = SparseVectorDotProduct()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
