"""Binary Search Tree with insertion, search, and traversals."""

class BSTNode:
    def __init__(self, key, val=None):
        self.key = key; self.val = val
        self.left = None; self.right = None

class BST:
    def __init__(self): self.root = None

    def insert(self, key, val=None):
        if not self.root: self.root = BSTNode(key, val); return
        cur = self.root
        while True:
            if key < cur.key:
                if not cur.left: cur.left = BSTNode(key, val); break
                cur = cur.left
            elif key > cur.key:
                if not cur.right: cur.right = BSTNode(key, val); break
                cur = cur.right
            else:
                cur.val = val; break

    def search(self, key):
        cur = self.root
        while cur:
            if key == cur.key: return cur.val
            elif key < cur.key: cur = cur.left
            else: cur = cur.right
        return None
