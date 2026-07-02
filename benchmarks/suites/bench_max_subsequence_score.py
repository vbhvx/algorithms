"""
Empirical benchmark for Maximum Subsequence Score MinHeap Sort
"""
import time
from algorithms.practice.heaps_and_priority.max_subsequence_score import solve_max_subsequence_score

def benchmark_max_subsequence_score():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_subsequence_score([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_subsequence_score()
    print(f"Maximum Subsequence Score MinHeap Sort 100 iterations took {t*1000:.3f}ms")
