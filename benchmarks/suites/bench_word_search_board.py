"""
Empirical benchmark for Word Search Matrix Grid Backtracking
"""
import time
from algorithms.practice.backtracking.word_search_board import solve_word_search_board

def benchmark_word_search_board():
    start = time.perf_counter()
    for _ in range(100):
        solve_word_search_board([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_word_search_board()
    print(f"Word Search Matrix Grid Backtracking 100 iterations took {t*1000:.3f}ms")
