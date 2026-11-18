# Partition Labels Last Seen Index

## Category
`two_pointers`

## Complexity
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(1)$

## Invariants & Approach
1. Record rightmost occurrence index of every character in first pass.
2. Maintain partition boundary dynamically as running max of seen character limits.
