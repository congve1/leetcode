class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_map = {}
        for idx, num in enumerate(nums):
            if nums_map.has_key(target-num):
                idy = nums_map.get(target-num)
                if idx != idy:
                    return [idy, idx]
            nums_map[num] = idx
        