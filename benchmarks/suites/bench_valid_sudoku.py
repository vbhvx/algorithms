"""
Empirical benchmark for Valid Sudoku Bitmask Checker
"""
import time
from algorithms.practice.arrays_and_hashing.valid_sudoku import solve_valid_sudoku

def benchmark_valid_sudoku():
    start = time.perf_counter()
    for _ in range(100):
        solve_valid_sudoku([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_valid_sudoku()
    print(f"Valid Sudoku Bitmask Checker 100 iterations took {t*1000:.3f}ms")
