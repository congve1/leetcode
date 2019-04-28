class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if not (num > 0 and num & (num-1) == 0):
            return False
        return (num & 0x55555555)