"""
Empirical benchmark for Hand of Straights Consecutive Groups MinHeap
"""
import time
from algorithms.practice.greedy_algorithms.hand_of_straights import solve_hand_of_straights

def benchmark_hand_of_straights():
    start = time.perf_counter()
    for _ in range(100):
        solve_hand_of_straights([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_hand_of_straights()
    print(f"Hand of Straights Consecutive Groups MinHeap 100 iterations took {t*1000:.3f}ms")
