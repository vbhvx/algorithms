"""
Empirical benchmark for Teemo Attacking Non-Overlapping Duration
"""
import time
from algorithms.practice.intervals_scheduling.teemo_attacking_poison import solve_teemo_attacking_poison

def benchmark_teemo_attacking_poison():
    start = time.perf_counter()
    for _ in range(100):
        solve_teemo_attacking_poison([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_teemo_attacking_poison()
    print(f"Teemo Attacking Non-Overlapping Duration 100 iterations took {t*1000:.3f}ms")
