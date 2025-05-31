"""Floyd's Tortoise and Hare cycle detection algorithm."""

def has_cycle(head) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False
