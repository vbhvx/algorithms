"""
Empirical benchmark for Design Browser History DLL Simulation
"""
import time
from algorithms.practice.linked_lists.design_browser_history import solve_design_browser_history

def benchmark_design_browser_history():
    start = time.perf_counter()
    for _ in range(100):
        solve_design_browser_history([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_design_browser_history()
    print(f"Design Browser History DLL Simulation 100 iterations took {t*1000:.3f}ms")
