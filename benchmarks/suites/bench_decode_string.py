"""
Empirical benchmark for Decode String Nested Multipliers
"""
import time
from algorithms.practice.stack_and_queue.decode_string import solve_decode_string

def benchmark_decode_string():
    start = time.perf_counter()
    for _ in range(100):
        solve_decode_string([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_decode_string()
    print(f"Decode String Nested Multipliers 100 iterations took {t*1000:.3f}ms")
