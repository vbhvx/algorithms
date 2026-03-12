"""
Empirical benchmark for Asteroid Collision Stack Simulation
"""
import time
from algorithms.practice.stack_and_queue.asteroid_collision import solve_asteroid_collision

def benchmark_asteroid_collision():
    start = time.perf_counter()
    for _ in range(100):
        solve_asteroid_collision([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_asteroid_collision()
    print(f"Asteroid Collision Stack Simulation 100 iterations took {t*1000:.3f}ms")
