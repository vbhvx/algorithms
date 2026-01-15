"""
Empirical benchmark for Ransom Note Frequency Match
"""
import time
from algorithms.practice.arrays_and_hashing.ransom_note import solve_ransom_note

def benchmark_ransom_note():
    start = time.perf_counter()
    for _ in range(100):
        solve_ransom_note([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_ransom_note()
    print(f"Ransom Note Frequency Match 100 iterations took {t*1000:.3f}ms")
