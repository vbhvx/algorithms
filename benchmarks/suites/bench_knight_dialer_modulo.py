"""
Empirical benchmark for Knight Dialer Graph Transitions
"""
import time
from algorithms.practice.dynamic_programming_1d.knight_dialer_modulo import solve_knight_dialer_modulo

def benchmark_knight_dialer_modulo():
    start = time.perf_counter()
    for _ in range(100):
        solve_knight_dialer_modulo([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_knight_dialer_modulo()
    print(f"Knight Dialer Graph Transitions 100 iterations took {t*1000:.3f}ms")
