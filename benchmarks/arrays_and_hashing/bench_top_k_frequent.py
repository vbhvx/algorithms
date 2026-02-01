"""Benchmark profile for Top K Frequent Elements Bucket Sort."""
import time
from src.arrays_and_hashing.top_k_frequent import TopKFrequentElementsBucketSort

def benchmark():
    solver = TopKFrequentElementsBucketSort()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
