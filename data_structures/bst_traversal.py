"""In-order, pre-order, and post-order iterators for binary trees."""

def inorder_traversal(root):
    res = []
    def dfs(n):
        if not n: return
        dfs(n.left); res.append(n.key); dfs(n.right)
    dfs(root); return res

def preorder_traversal(root):
    res = []
    def dfs(n):
        if not n: return
        res.append(n.key); dfs(n.left); dfs(n.right)
    dfs(root); return res
