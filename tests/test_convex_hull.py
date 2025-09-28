from algorithms.math_geometry.convex_hull import convex_hull

def test_convex_hull():
    pts = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
    hull = convex_hull(pts)
    assert (0, 0) in hull and (3, 0) in hull and (3, 3) in hull and (0, 3) in hull
