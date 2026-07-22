"""
Empirical benchmark for Gray Code Generation Reflection Backtrack
"""
import time
from algorithms.practice.backtracking.gray_code_sequence import solve_gray_code_sequence

def benchmark_gray_code_sequence():
    start = time.perf_counter()
    for _ in range(100):
        solve_gray_code_sequence([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_gray_code_sequence()
    print(f"Gray Code Generation Reflection Backtrack 100 iterations took {t*1000:.3f}ms")
