"""
Empirical benchmark for Champagne Tower Pascal Overflow Simulation
"""
import time
from algorithms.practice.dynamic_programming_2d.champagne_tower_flow import solve_champagne_tower_flow

def benchmark_champagne_tower_flow():
    start = time.perf_counter()
    for _ in range(100):
        solve_champagne_tower_flow([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_champagne_tower_flow()
    print(f"Champagne Tower Pascal Overflow Simulation 100 iterations took {t*1000:.3f}ms")
