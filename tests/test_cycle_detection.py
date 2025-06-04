from data_structures.singly_linked_list import ListNode
from data_structures.cycle_detection import has_cycle

def test_cycle_detection():
    n1 = ListNode(1); n2 = ListNode(2); n3 = ListNode(3)
    n1.next = n2; n2.next = n3
    assert not has_cycle(n1)
    n3.next = n1
    assert has_cycle(n1)
