# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            return res
        return inorder(root)
        """
        """
        https://juejin.im/post/59e3fde451882578c20858a5
        """
        cur = root
        res = []
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            p = stack.pop()
            res.append(p.val)
            cur = p.right
        return res
