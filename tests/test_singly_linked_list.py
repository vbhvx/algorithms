from data_structures.singly_linked_list import SinglyLinkedList

def test_singly_linked_list():
    ll = SinglyLinkedList()
    for i in [1, 2, 3]: ll.append(i)
    assert ll.to_list() == [1, 2, 3]
    ll.reverse()
    assert ll.to_list() == [3, 2, 1]
