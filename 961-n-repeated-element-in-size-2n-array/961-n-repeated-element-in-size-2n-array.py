class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        """        
        counts = [0 for _ in range(10000)]
        res = None
        for num in A:
            counts[num] += 1
            if counts[num] == 2:
                res = num
                break
        return res
        """
        """        
        A = sorted(A)
        if A[0] == A[1]:
            return A[0]
        return A[int(len(A)/2)]
        """
        res = set()
        for a in A:
            if a in res:
                return a
            res.add(a)
        