"""
Empirical benchmark for Data Stream as Disjoint Intervals BST
"""
import time
from algorithms.practice.intervals_scheduling.data_stream_intervals import solve_data_stream_intervals

def benchmark_data_stream_intervals():
    start = time.perf_counter()
    for _ in range(100):
        solve_data_stream_intervals([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_data_stream_intervals()
    print(f"Data Stream as Disjoint Intervals BST 100 iterations took {t*1000:.3f}ms")
