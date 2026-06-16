"""
Empirical benchmark for Remove Sub-Folders from Filesystem Trie
"""
import time
from algorithms.practice.tries_and_prefix.remove_sub_folders import solve_remove_sub_folders

def benchmark_remove_sub_folders():
    start = time.perf_counter()
    for _ in range(100):
        solve_remove_sub_folders([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_remove_sub_folders()
    print(f"Remove Sub-Folders from Filesystem Trie 100 iterations took {t*1000:.3f}ms")
