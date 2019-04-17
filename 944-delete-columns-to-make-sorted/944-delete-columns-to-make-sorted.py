class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        """
        count = 0
        for i in range(len(A[0])):
            for j in range(1, len(A)):
                if ord(A[j-1][i]) > ord(A[j][i]):
                    count += 1
                    break
        return count
        """
        count = 0
        for chs in zip(*A):
            if sorted(chs) != list(chs):
                count += 1
        return count

        