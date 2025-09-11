from algorithms.strings.z_algorithm import compute_z_array

def test_z_array():
    s = "aab$aabxaaab"
    z = compute_z_array(s)
    assert z[4] == 3
