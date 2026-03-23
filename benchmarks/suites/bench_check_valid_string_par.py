"""
Empirical benchmark for Valid Parenthesis String Wildcards
"""
import time
from algorithms.practice.stack_and_queue.check_valid_string_par import solve_check_valid_string_par

def benchmark_check_valid_string_par():
    start = time.perf_counter()
    for _ in range(100):
        solve_check_valid_string_par([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_check_valid_string_par()
    print(f"Valid Parenthesis String Wildcards 100 iterations took {t*1000:.3f}ms")
