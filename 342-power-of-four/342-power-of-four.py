class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if not (n > 0 and n & (n-1) == 0):
            return False
        return (n & 0x55555555)