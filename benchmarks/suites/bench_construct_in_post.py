"""
Empirical benchmark for Construct Binary Tree from Inorder Postorder
"""
import time
from algorithms.practice.trees_and_bst.construct_in_post import solve_construct_in_post

def benchmark_construct_in_post():
    start = time.perf_counter()
    for _ in range(100):
        solve_construct_in_post([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_construct_in_post()
    print(f"Construct Binary Tree from Inorder Postorder 100 iterations took {t*1000:.3f}ms")
