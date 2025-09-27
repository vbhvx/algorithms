"""Graham Scan algorithm finding the 2D convex hull of a set of points."""
from typing import List, Tuple

def orientation(p, q, r) -> int:
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0: return 0
    return 1 if val > 0 else 2 # 1: Clockwise, 2: Counterclockwise

def convex_hull(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    pts = sorted(set(points))
    if len(pts) <= 1: return pts
    lower = []
    for p in pts:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) != 2:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) != 2:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]
