"""Benchmark profile for Ransom Note Frequency Match."""
import time
from src.arrays_and_hashing.ransom_note import RansomNoteFrequencyMatch

def benchmark():
    solver = RansomNoteFrequencyMatch()
    t0 = time.time()
    for _ in range(1000):
        solver.solve()
    return time.time() - t0

if __name__ == "__main__":
    elapsed = benchmark()
    print(f"Elapsed: {elapsed:.4f}s")
