"""
Empirical benchmark for Letter Combinations of a Phone Number
"""
import time
from algorithms.practice.backtracking.letter_combos_phone import solve_letter_combos_phone

def benchmark_letter_combos_phone():
    start = time.perf_counter()
    for _ in range(100):
        solve_letter_combos_phone([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_letter_combos_phone()
    print(f"Letter Combinations of a Phone Number 100 iterations took {t*1000:.3f}ms")
