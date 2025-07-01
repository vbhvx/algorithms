from data_structures.singly_linked_list import ListNode
from data_structures.merge_lists import merge_two_lists

def test_merge_two_lists():
    l1 = ListNode(1, ListNode(3))
    l2 = ListNode(2, ListNode(4))
    m = merge_two_lists(l1, l2)
    res = []
    while m: res.append(m.val); m = m.next
    assert res == [1, 2, 3, 4]
