from data_structures.singly_linked_list import ListNode
from data_structures.linked_list_middle import find_middle_node

def test_middle_node():
    n = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert find_middle_node(n).val == 3
