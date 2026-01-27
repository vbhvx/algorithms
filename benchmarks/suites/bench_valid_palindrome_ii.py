"""
Empirical benchmark for Valid Palindrome II Skip
"""
import time
from algorithms.practice.two_pointers.valid_palindrome_ii import solve_valid_palindrome_ii

def benchmark_valid_palindrome_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_valid_palindrome_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_valid_palindrome_ii()
    print(f"Valid Palindrome II Skip 100 iterations took {t*1000:.3f}ms")
