"""
Empirical benchmark for Serialize and Deserialize Binary Tree BFS
"""
import time
from algorithms.practice.trees_and_bst.serialize_deserialize import solve_serialize_deserialize

def benchmark_serialize_deserialize():
    start = time.perf_counter()
    for _ in range(100):
        solve_serialize_deserialize([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_serialize_deserialize()
    print(f"Serialize and Deserialize Binary Tree BFS 100 iterations took {t*1000:.3f}ms")
