"""
Empirical benchmark for Top K Frequent Words MinHeap Tiebreaker
"""
import time
from algorithms.practice.heaps_and_priority.top_k_frequent_words import solve_top_k_frequent_words

def benchmark_top_k_frequent_words():
    start = time.perf_counter()
    for _ in range(100):
        solve_top_k_frequent_words([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_top_k_frequent_words()
    print(f"Top K Frequent Words MinHeap Tiebreaker 100 iterations took {t*1000:.3f}ms")
