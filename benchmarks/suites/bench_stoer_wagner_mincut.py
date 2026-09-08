"""
Empirical benchmark for Stoer-Wagner Global Minimum Cut Algorithm
"""
import time
from algorithms.practice.network_flow_matching.stoer_wagner_mincut import solve_stoer_wagner_mincut

def benchmark_stoer_wagner_mincut():
    start = time.perf_counter()
    for _ in range(100):
        solve_stoer_wagner_mincut([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_stoer_wagner_mincut()
    print(f"Stoer-Wagner Global Minimum Cut Algorithm 100 iterations took {t*1000:.3f}ms")
