"""
Empirical benchmark for Maximum Score Words Formed by Letters
"""
import time
from algorithms.practice.backtracking.max_score_words_letters import solve_max_score_words_letters

def benchmark_max_score_words_letters():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_score_words_letters([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_score_words_letters()
    print(f"Maximum Score Words Formed by Letters 100 iterations took {t*1000:.3f}ms")
