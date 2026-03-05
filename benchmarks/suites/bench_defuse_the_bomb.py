"""
Empirical benchmark for Defuse the Bomb Sliding Sum
"""
import time
from algorithms.practice.sliding_window.defuse_the_bomb import solve_defuse_the_bomb

def benchmark_defuse_the_bomb():
    start = time.perf_counter()
    for _ in range(100):
        solve_defuse_the_bomb([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_defuse_the_bomb()
    print(f"Defuse the Bomb Sliding Sum 100 iterations took {t*1000:.3f}ms")
