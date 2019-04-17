class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        min_int = 2**31-1
        counts = [min_int for _ in range(26)]
        #print(counts)
        for word in A:
            temp = [0 for _ in range(26)]
            for c in word:
                temp[(ord(c))%ord('a')] += 1
            for i in range(26):
                #print(temp[i], counts[i])
                if counts[i] > temp[i]:
                    counts[i] = temp[i]
        res = []
        for i in range(26):
            if counts[i] != min_int:
                for _ in range(counts[i]):
                    res.append(chr(i+ord('a')))
        return res
        