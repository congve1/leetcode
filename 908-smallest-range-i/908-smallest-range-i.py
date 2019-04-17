class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        max_num = -200000
        min_num = 200000
        for num in A:
            if num > max_num:
                max_num = num
            if num < min_num:
                min_num = num
        diff = max_num - min_num - 2*K
        diff = 0 if diff < 0 else diff
        
        return diff
        
        