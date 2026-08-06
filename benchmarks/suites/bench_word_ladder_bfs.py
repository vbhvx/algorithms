"""
Empirical benchmark for Word Ladder Shortest Transformation BFS
"""
import time
from algorithms.practice.graphs_and_traversals.word_ladder_bfs import solve_word_ladder_bfs

def benchmark_word_ladder_bfs():
    start = time.perf_counter()
    for _ in range(100):
        solve_word_ladder_bfs([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_word_ladder_bfs()
    print(f"Word Ladder Shortest Transformation BFS 100 iterations took {t*1000:.3f}ms")
