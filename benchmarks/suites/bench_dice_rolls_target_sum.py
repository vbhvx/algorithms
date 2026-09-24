"""
Empirical benchmark for Number of Dice Rolls with Target Sum
"""
import time
from algorithms.practice.dynamic_programming_1d.dice_rolls_target_sum import solve_dice_rolls_target_sum

def benchmark_dice_rolls_target_sum():
    start = time.perf_counter()
    for _ in range(100):
        solve_dice_rolls_target_sum([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_dice_rolls_target_sum()
    print(f"Number of Dice Rolls with Target Sum 100 iterations took {t*1000:.3f}ms")
