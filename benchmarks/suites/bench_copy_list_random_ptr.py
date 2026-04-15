"""
Empirical benchmark for Copy List with Random Pointer O1 Space
"""
import time
from algorithms.practice.linked_lists.copy_list_random_ptr import solve_copy_list_random_ptr

def benchmark_copy_list_random_ptr():
    start = time.perf_counter()
    for _ in range(100):
        solve_copy_list_random_ptr([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_copy_list_random_ptr()
    print(f"Copy List with Random Pointer O1 Space 100 iterations took {t*1000:.3f}ms")
