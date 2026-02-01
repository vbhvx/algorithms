"""
Empirical benchmark for Move Zeroes In Place
"""
import time
from algorithms.practice.two_pointers.move_zeroes import solve_move_zeroes

def benchmark_move_zeroes():
    start = time.perf_counter()
    for _ in range(100):
        solve_move_zeroes([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_move_zeroes()
    print(f"Move Zeroes In Place 100 iterations took {t*1000:.3f}ms")
