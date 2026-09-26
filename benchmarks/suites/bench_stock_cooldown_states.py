"""
Empirical benchmark for Best Time Stock with Cooldown 3 States
"""
import time
from algorithms.practice.dynamic_programming_2d.stock_cooldown_states import solve_stock_cooldown_states

def benchmark_stock_cooldown_states():
    start = time.perf_counter()
    for _ in range(100):
        solve_stock_cooldown_states([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_stock_cooldown_states()
    print(f"Best Time Stock with Cooldown 3 States 100 iterations took {t*1000:.3f}ms")
