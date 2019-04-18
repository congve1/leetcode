"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        queue = [[root]]
        while queue:
            nodes = queue.pop(0)
            temp_val = []
            temp = []
            for node in nodes:
                temp_val.append(node.val)
                if node.children:
                    for child in node.children:
                        temp.append(child)
            if temp:
                queue.append(temp)
            res.append(temp_val)
        return res