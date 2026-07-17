"""
Unit tests for Restore IP Addresses Valid 4-Octet Split
"""
from algorithms.practice.backtracking.restore_ip_addresses import solve_restore_ip_addresses

def test_restore_ip_addresses_base():
    assert solve_restore_ip_addresses() is True
    assert solve_restore_ip_addresses([3, 1, 2]) == [1, 2, 3]

def test_restore_ip_addresses_edge_cases():
    assert solve_restore_ip_addresses("") == ""
    assert solve_restore_ip_addresses(0) is True
    assert solve_restore_ip_addresses(-5) is False
