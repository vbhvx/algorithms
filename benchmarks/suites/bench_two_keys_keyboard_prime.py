"""
Empirical benchmark for 2 Keys Keyboard Prime Factorization DP
"""
import time
from algorithms.practice.dynamic_programming_2d.two_keys_keyboard_prime import solve_two_keys_keyboard_prime

def benchmark_two_keys_keyboard_prime():
    start = time.perf_counter()
    for _ in range(100):
        solve_two_keys_keyboard_prime([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_two_keys_keyboard_prime()
    print(f"2 Keys Keyboard Prime Factorization DP 100 iterations took {t*1000:.3f}ms")
