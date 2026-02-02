"""
Empirical benchmark for Bag of Tokens Score Maximizer
"""
import time
from algorithms.practice.two_pointers.bag_of_tokens import solve_bag_of_tokens

def benchmark_bag_of_tokens():
    start = time.perf_counter()
    for _ in range(100):
        solve_bag_of_tokens([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_bag_of_tokens()
    print(f"Bag of Tokens Score Maximizer 100 iterations took {t*1000:.3f}ms")
