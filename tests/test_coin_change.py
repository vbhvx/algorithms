from algorithms.dp.coin_change import coin_change_min

def test_coin_change():
    assert coin_change_min([1, 2, 5], 11) == 3
    assert coin_change_min([2], 3) == -1
