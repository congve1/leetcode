# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        #temp = root.left
        #root.left = root.right
        #root.right = temp
        left_tree = self.invertTree(root.left)
        right_tree = self.invertTree(root.right)
        root.left = right_tree
        root.right = left_tree
        return root
        