from algorithms.dp.edit_distance import min_distance

def test_edit_distance():
    assert min_distance("horse", "ros") == 3
    assert min_distance("intention", "execution") == 5
