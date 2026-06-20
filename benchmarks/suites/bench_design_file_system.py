"""
Empirical benchmark for Design File System Trie Path Registry
"""
import time
from algorithms.practice.tries_and_prefix.design_file_system import solve_design_file_system

def benchmark_design_file_system():
    start = time.perf_counter()
    for _ in range(100):
        solve_design_file_system([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_design_file_system()
    print(f"Design File System Trie Path Registry 100 iterations took {t*1000:.3f}ms")
