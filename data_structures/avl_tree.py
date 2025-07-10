"""AVL Tree with height balancing and single/double rotations."""

class AVLNode:
    def __init__(self, key):
        self.key = key; self.height = 1
        self.left = None; self.right = None

class AVLTree:
    def _height(self, n): return n.height if n else 0
    def _balance(self, n): return self._height(n.left) - self._height(n.right) if n else 0

    def _rotate_right(self, y):
        x = y.left; T2 = x.right
        x.right = y; y.left = T2
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        return x

    def _rotate_left(self, x):
        y = x.right; T2 = y.left
        y.left = x; x.right = T2
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def insert(self, root, key):
        if not root: return AVLNode(key)
        if key < root.key: root.left = self.insert(root.left, key)
        elif key > root.key: root.right = self.insert(root.right, key)
        else: return root
        root.height = 1 + max(self._height(root.left), self._height(root.right))
        b = self._balance(root)
        if b > 1 and key < root.left.key: return self._rotate_right(root)
        if b < -1 and key > root.right.key: return self._rotate_left(root)
        if b > 1 and key > root.left.key:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)
        if b < -1 and key < root.right.key:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)
        return root
