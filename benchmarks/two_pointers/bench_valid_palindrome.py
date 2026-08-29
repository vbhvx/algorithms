"""Benchmark profile for Valid Palindrome Alphanumeric."""
import time
from src.two_pointers.valid_palindrome import ValidPalindromeAlphanumeric

def benchmark():
    solver = ValidPalindromeAlphanumeric()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
