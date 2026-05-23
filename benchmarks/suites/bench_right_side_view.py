"""
Empirical benchmark for Binary Tree Right Side View Level Order
"""
import time
from algorithms.practice.trees_and_bst.right_side_view import solve_right_side_view

def benchmark_right_side_view():
    start = time.perf_counter()
    for _ in range(100):
        solve_right_side_view([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_right_side_view()
    print(f"Binary Tree Right Side View Level Order 100 iterations took {t*1000:.3f}ms")
