"""
Empirical benchmark for Encode Decode Strings Framing
"""
import time
from algorithms.practice.arrays_and_hashing.encode_decode_strings import solve_encode_decode_strings

def benchmark_encode_decode_strings():
    start = time.perf_counter()
    for _ in range(100):
        solve_encode_decode_strings([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_encode_decode_strings()
    print(f"Encode Decode Strings Framing 100 iterations took {t*1000:.3f}ms")
