class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        res = 0
        nums = sorted(nums)
        mid = len(nums)//2
        for i in range(mid):
            res += nums[2*i]
        return res
     
        