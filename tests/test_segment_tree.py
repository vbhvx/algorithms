from data_structures.segment_tree import SegmentTree

def test_segment_tree():
    arr = [1, 3, 2, 7, 9, 11]
    st = SegmentTree(arr)
    assert st.query(0, 0, len(arr) - 1, 1, 5) == 2
    assert st.query(0, 0, len(arr) - 1, 3, 5) == 7
