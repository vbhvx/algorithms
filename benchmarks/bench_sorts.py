from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.quick_sort import quick_sort
import time, random
def bench_sorting():
    arr = [random.randint(1, 1000) for _ in range(500)]
    t0 = time.perf_counter(); merge_sort(arr); t1 = time.perf_counter()
    return t1 - t0
