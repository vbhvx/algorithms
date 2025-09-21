"""Combination sum with unlimited candidate reuse."""
from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    def backtrack(start, cur_target, path):
        if cur_target == 0: res.append(list(path)); return
        for i in range(start, len(candidates)):
            c = candidates[i]
            if c <= cur_target:
                path.append(c)
                backtrack(i, cur_target - c, path)
                path.pop()
    backtrack(0, target, []); return res
