"""
Empirical benchmark for Palindrome Linked List In Place Mid Reverse
"""
import time
from algorithms.practice.linked_lists.palindrome_linked_list import solve_palindrome_linked_list

def benchmark_palindrome_linked_list():
    start = time.perf_counter()
    for _ in range(100):
        solve_palindrome_linked_list([i for i in range(100)])
    elapsed = time.perf_counter() - start
    return elapsed

if __name__ == "__main__":
    t = benchmark_palindrome_linked_list()
    print(f"Palindrome Linked List In Place Mid Reverse 100 iterations took {t*1000:.3f}ms")
