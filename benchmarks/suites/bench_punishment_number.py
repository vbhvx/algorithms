"""
Empirical benchmark for Find the Punishment Number of an Integer
"""
import time
from algorithms.practice.backtracking.punishment_number import solve_punishment_number

def benchmark_punishment_number():
    start = time.perf_counter()
    for _ in range(100):
        solve_punishment_number([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_punishment_number()
    print(f"Find the Punishment Number of an Integer 100 iterations took {t*1000:.3f}ms")
