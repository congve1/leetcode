class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set_1 = set(nums1)
        set_2 = set(nums2)
        return list(set_1.intersection(set_2))
        