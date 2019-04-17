# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #if root is None:
        #    return 0
        #left_max = self.maxDepth(root.left)+1
        #right_max = self.maxDepth(root.right)+1
        #return max((left_max,right_max))
        stack = []
        depth = 0
        if root is not None:
            stack.append((1, root))
        while stack:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth+1, root.left))
                stack.append((current_depth+1, root.right))
        return depth
        