"""
Empirical benchmark for Student Attendance Record II Matrix DP
"""
import time
from algorithms.practice.dynamic_programming_1d.student_attendance_ii import solve_student_attendance_ii

def benchmark_student_attendance_ii():
    start = time.perf_counter()
    for _ in range(100):
        solve_student_attendance_ii([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_student_attendance_ii()
    print(f"Student Attendance Record II Matrix DP 100 iterations took {t*1000:.3f}ms")
