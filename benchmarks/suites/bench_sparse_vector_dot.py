"""
Empirical benchmark for Sparse Vector Dot Product
"""
import time
from algorithms.practice.arrays_and_hashing.sparse_vector_dot import solve_sparse_vector_dot

def benchmark_sparse_vector_dot():
    start = time.perf_counter()
    for _ in range(100):
        solve_sparse_vector_dot([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_sparse_vector_dot()
    print(f"Sparse Vector Dot Product 100 iterations took {t*1000:.3f}ms")
