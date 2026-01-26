"""
Empirical benchmark for Valid Palindrome Alphanumeric
"""
import time
from algorithms.practice.two_pointers.valid_palindrome import solve_valid_palindrome

def benchmark_valid_palindrome():
    start = time.perf_counter()
    for _ in range(100):
        solve_valid_palindrome([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_valid_palindrome()
    print(f"Valid Palindrome Alphanumeric 100 iterations took {t*1000:.3f}ms")
