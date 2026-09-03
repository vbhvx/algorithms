"""
Empirical benchmark for Circulation with Demands Lower Upper Bounds
"""
import time
from algorithms.practice.network_flow_matching.circulation_with_demands import solve_circulation_with_demands

def benchmark_circulation_with_demands():
    start = time.perf_counter()
    for _ in range(100):
        solve_circulation_with_demands([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_circulation_with_demands()
    print(f"Circulation with Demands Lower Upper Bounds 100 iterations took {t*1000:.3f}ms")
