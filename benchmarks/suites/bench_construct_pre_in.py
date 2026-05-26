"""
Empirical benchmark for Construct Binary Tree from Preorder Inorder
"""
import time
from algorithms.practice.trees_and_bst.construct_pre_in import solve_construct_pre_in

def benchmark_construct_pre_in():
    start = time.perf_counter()
    for _ in range(100):
        solve_construct_pre_in([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_construct_pre_in()
    print(f"Construct Binary Tree from Preorder Inorder 100 iterations took {t*1000:.3f}ms")
