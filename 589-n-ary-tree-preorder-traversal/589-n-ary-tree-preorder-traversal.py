"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """
                res = []
        def rec(root):
            if root is None:
                return []
            res.append(root.val)
            if root.children:
                for child in root.children:
                    rec(child)
        rec(root)
        return res
        """
        if root is None:
            return []
        stack = []
        res = []
        stack.append(root)
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.children:
                for child in root.children[::-1]:
                    stack.append(child)
        return res

    
        