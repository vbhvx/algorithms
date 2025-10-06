from collections import defaultdict
def find_target_sum_ways(nums, target):
    dp = {0: 1}
    for x in nums:
        nxt = defaultdict(int)
        for s, cnt in dp.items(): nxt[s + x] += cnt; nxt[s - x] += cnt
        dp = nxt
    return dp.get(target, 0)
