"""
Empirical benchmark for Maximum XOR With an Element From Array Offline
"""
import time
from algorithms.practice.tries_and_prefix.max_xor_element_arr import solve_max_xor_element_arr

def benchmark_max_xor_element_arr():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_xor_element_arr([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_xor_element_arr()
    print(f"Maximum XOR With an Element From Array Offline 100 iterations took {t*1000:.3f}ms")
