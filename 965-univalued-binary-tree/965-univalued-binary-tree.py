# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        val = root.val
        queue = collections.deque()
        queue.append(root)
        while queue:
            root = queue.popleft()
            if root.val != val:
                return False
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return True
        """
        def inner(root, val):
            if not root:
                return True
            if root.val != val:
                return False
            return inner(root.left, val) and inner(root.right, val)
        if not root:
            return True
        return inner(root, root.val)
        