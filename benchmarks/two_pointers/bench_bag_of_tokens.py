"""Benchmark profile for Bag of Tokens Score Maximizer."""
import time
from src.two_pointers.bag_of_tokens import BagOfTokensScoreMaximizer

def benchmark():
    solver = BagOfTokensScoreMaximizer()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
