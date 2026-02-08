"""
Empirical benchmark for Reverse Only Letters Conditional
"""
import time
from algorithms.practice.two_pointers.reverse_only_letters import solve_reverse_only_letters

def benchmark_reverse_only_letters():
    start = time.perf_counter()
    for _ in range(100):
        solve_reverse_only_letters([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_reverse_only_letters()
    print(f"Reverse Only Letters Conditional 100 iterations took {t*1000:.3f}ms")
