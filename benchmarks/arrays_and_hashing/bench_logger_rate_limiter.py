"""Benchmark profile for Logger Rate Limiter Lookup."""
import time
from src.arrays_and_hashing.logger_rate_limiter import LoggerRateLimiterLookup

def benchmark():
    solver = LoggerRateLimiterLookup()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
