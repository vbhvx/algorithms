"""
Empirical benchmark for Palindrome Partitioning DFS Memo
"""
import time
from algorithms.practice.backtracking.palindrome_partition import solve_palindrome_partition

def benchmark_palindrome_partition():
    start = time.perf_counter()
    for _ in range(100):
        solve_palindrome_partition([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_palindrome_partition()
    print(f"Palindrome Partitioning DFS Memo 100 iterations took {t*1000:.3f}ms")
