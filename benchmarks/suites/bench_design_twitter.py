"""
Empirical benchmark for Design Twitter Feed Priority Queue Merge
"""
import time
from algorithms.practice.heaps_and_priority.design_twitter import solve_design_twitter

def benchmark_design_twitter():
    start = time.perf_counter()
    for _ in range(100):
        solve_design_twitter([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_design_twitter()
    print(f"Design Twitter Feed Priority Queue Merge 100 iterations took {t*1000:.3f}ms")
