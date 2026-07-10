"""
Empirical benchmark for Mice and Cheese Greedy MaxHeap Difference
"""
import time
from algorithms.practice.heaps_and_priority.mice_and_cheese import solve_mice_and_cheese

def benchmark_mice_and_cheese():
    start = time.perf_counter()
    for _ in range(100):
        solve_mice_and_cheese([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_mice_and_cheese()
    print(f"Mice and Cheese Greedy MaxHeap Difference 100 iterations took {t*1000:.3f}ms")
