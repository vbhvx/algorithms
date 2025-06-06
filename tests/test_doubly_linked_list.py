from data_structures.doubly_linked_list import DoublyLinkedList

def test_doubly_linked_list():
    dll = DoublyLinkedList()
    dll.append("a"); dll.append("b")
    assert dll.size == 2
    dll.remove(dll.head.next)
    assert dll.size == 1
