"""
Empirical benchmark for Project Selection Problem Profit Maximization
"""
import time
from algorithms.practice.network_flow_matching.project_selection_flow import solve_project_selection_flow

def benchmark_project_selection_flow():
    start = time.perf_counter()
    for _ in range(100):
        solve_project_selection_flow([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_project_selection_flow()
    print(f"Project Selection Problem Profit Maximization 100 iterations took {t*1000:.3f}ms")
