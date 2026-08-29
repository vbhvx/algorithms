"""Benchmark profile for Valid Palindrome II Skip."""
import time
from src.two_pointers.valid_palindrome_ii import ValidPalindromeIiSkip

def benchmark():
    solver = ValidPalindromeIiSkip()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
