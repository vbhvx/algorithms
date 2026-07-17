"""
Empirical benchmark for Sudoku Solver 9x9 Constraint Propagation
"""
import time
from algorithms.practice.backtracking.sudoku_solver_exact import solve_sudoku_solver_exact

def benchmark_sudoku_solver_exact():
    start = time.perf_counter()
    for _ in range(100):
        solve_sudoku_solver_exact([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_sudoku_solver_exact()
    print(f"Sudoku Solver 9x9 Constraint Propagation 100 iterations took {t*1000:.3f}ms")
