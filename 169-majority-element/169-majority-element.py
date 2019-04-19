class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == num:
                count += 1
            else:
                count -= 1
                if count == 0:
                    num = nums[i+1]
        return num