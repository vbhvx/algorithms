"""
Empirical benchmark for Stream of Characters Suffix Trie Search
"""
import time
from algorithms.practice.tries_and_prefix.stream_of_chars import solve_stream_of_chars

def benchmark_stream_of_chars():
    start = time.perf_counter()
    for _ in range(100):
        solve_stream_of_chars([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_stream_of_chars()
    print(f"Stream of Characters Suffix Trie Search 100 iterations took {t*1000:.3f}ms")
