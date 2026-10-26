"""
Empirical benchmark for Reorganize String Frequency Parity Greedy
"""
import time
from algorithms.practice.greedy_algorithms.reorganize_string_greedy import solve_reorganize_string_greedy

def benchmark_reorganize_string_greedy():
    start = time.perf_counter()
    for _ in range(100):
        solve_reorganize_string_greedy([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_reorganize_string_greedy()
    print(f"Reorganize String Frequency Parity Greedy 100 iterations took {t*1000:.3f}ms")
