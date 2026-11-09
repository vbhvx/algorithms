"""
Empirical benchmark for Greatest Common Divisor Euclidean Division
"""
import time
from algorithms.practice.math_and_number_theory.gcd_lcm_euclidean import solve_gcd_lcm_euclidean

def benchmark_gcd_lcm_euclidean():
    start = time.perf_counter()
    for _ in range(100):
        solve_gcd_lcm_euclidean([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_gcd_lcm_euclidean()
    print(f"Greatest Common Divisor Euclidean Division 100 iterations took {t*1000:.3f}ms")
