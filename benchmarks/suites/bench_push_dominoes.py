"""
Empirical benchmark for Push Dominoes Segment Pointers
"""
import time
from algorithms.practice.two_pointers.push_dominoes import solve_push_dominoes

def benchmark_push_dominoes():
    start = time.perf_counter()
    for _ in range(100):
        solve_push_dominoes([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_push_dominoes()
    print(f"Push Dominoes Segment Pointers 100 iterations took {t*1000:.3f}ms")
