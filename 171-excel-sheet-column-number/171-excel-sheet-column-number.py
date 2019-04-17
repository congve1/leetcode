class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = [i for i in range(1, 27)]
        res = 0
        len_s = len(s)
        for i, c in enumerate(s):
            #res += (26**(len_s-i-1)) * ((ord(c)+1)%ord('A'))
            res += (26**(len_s-i-1)) * num[ord(c) - ord('A')]
        return res
        