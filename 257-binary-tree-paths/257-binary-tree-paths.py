# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        cur = []
        ans = []
        def dfs(node):
            if not node:
                return ans
            cur.append(str(node.val))
            if not node.left and not node.right:
                ans.append('->'.join(cur))
            dfs(node.left)
            dfs(node.right)
            cur.pop()
            return ans
        return dfs(root)