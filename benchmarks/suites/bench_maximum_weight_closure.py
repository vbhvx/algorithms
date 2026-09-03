"""
Empirical benchmark for Maximum Weight Closure in Directed Graph
"""
import time
from algorithms.practice.network_flow_matching.maximum_weight_closure import solve_maximum_weight_closure

def benchmark_maximum_weight_closure():
    start = time.perf_counter()
    for _ in range(100):
        solve_maximum_weight_closure([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_maximum_weight_closure()
    print(f"Maximum Weight Closure in Directed Graph 100 iterations took {t*1000:.3f}ms")
