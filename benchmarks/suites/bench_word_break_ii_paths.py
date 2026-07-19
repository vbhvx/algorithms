"""
Empirical benchmark for Word Break II Sentence Generation DFS
"""
import time
from algorithms.practice.backtracking.word_break_ii_paths import solve_word_break_ii_paths

def benchmark_word_break_ii_paths():
    start = time.perf_counter()
    for _ in range(100):
        solve_word_break_ii_paths([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_word_break_ii_paths()
    print(f"Word Break II Sentence Generation DFS 100 iterations took {t*1000:.3f}ms")
