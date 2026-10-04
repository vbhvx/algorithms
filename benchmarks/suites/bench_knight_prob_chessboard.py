"""
Empirical benchmark for Knight Probability in Chessboard Matrix
"""
import time
from algorithms.practice.dynamic_programming_2d.knight_prob_chessboard import solve_knight_prob_chessboard

def benchmark_knight_prob_chessboard():
    start = time.perf_counter()
    for _ in range(100):
        solve_knight_prob_chessboard([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_knight_prob_chessboard()
    print(f"Knight Probability in Chessboard Matrix 100 iterations took {t*1000:.3f}ms")
