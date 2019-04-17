class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for s in S:
            for j in J:
                if s == j:
                    count += 1
                    break
        return count
        