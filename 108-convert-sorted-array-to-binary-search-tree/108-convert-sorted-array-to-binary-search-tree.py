# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        len_s = len(nums)
        mid = len_s // 2
        left = 0
        right = len_s - 1        
        root = TreeNode(nums[mid])
        if len_s == 1:
            return root
        #print(nums[left:mid])
        #print(nums[mid+1:] if mid+1<=right else [])
        root.left = self.sortedArrayToBST(nums[left:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:] if mid+1<=right else [])
        return root
            
        