"""
Empirical benchmark for Resident Matching with Capacities and Ties
"""
import time
from algorithms.practice.network_flow_matching.resident_hospital_match import solve_resident_hospital_match

def benchmark_resident_hospital_match():
    start = time.perf_counter()
    for _ in range(100):
        solve_resident_hospital_match([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_resident_hospital_match()
    print(f"Resident Matching with Capacities and Ties 100 iterations took {t*1000:.3f}ms")
