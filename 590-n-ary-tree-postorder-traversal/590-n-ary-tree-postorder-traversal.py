"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    
    def postorder(self, root: 'Node') -> List[int]:
        """
        res = []
        def rec(root):
            if root is None:
                return res
            if root.children:
                for child in root.children:
                    rec(child)
            res.append(root.val)
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
            if root.children:
                for child in root.children:
                    stack.append(child)
            res.append(root.val)
        return res[::-1]
        