"""
Empirical benchmark for Word Ladder II Bidirectional BFS Backtrack
"""
import time
from algorithms.practice.graphs_and_traversals.word_ladder_ii_paths import solve_word_ladder_ii_paths

def benchmark_word_ladder_ii_paths():
    start = time.perf_counter()
    for _ in range(100):
        solve_word_ladder_ii_paths([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_word_ladder_ii_paths()
    print(f"Word Ladder II Bidirectional BFS Backtrack 100 iterations took {t*1000:.3f}ms")
