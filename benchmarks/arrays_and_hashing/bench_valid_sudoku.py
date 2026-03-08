"""Benchmark profile for Valid Sudoku Bitmask Checker."""
import time
from src.arrays_and_hashing.valid_sudoku import ValidSudokuBitmaskChecker

def benchmark():
    solver = ValidSudokuBitmaskChecker()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
