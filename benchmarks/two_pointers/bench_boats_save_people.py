"""Benchmark profile for Boats to Save People Pairing."""
import time
from src.two_pointers.boats_save_people import BoatsToSavePeoplePairing

def benchmark():
    solver = BoatsToSavePeoplePairing()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
