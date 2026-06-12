"""
Empirical benchmark for Maximum XOR of Two Numbers in Array Bit Trie
"""
import time
from algorithms.practice.tries_and_prefix.max_xor_two_nums import solve_max_xor_two_nums

def benchmark_max_xor_two_nums():
    start = time.perf_counter()
    for _ in range(100):
        solve_max_xor_two_nums([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_max_xor_two_nums()
    print(f"Maximum XOR of Two Numbers in Array Bit Trie 100 iterations took {t*1000:.3f}ms")
