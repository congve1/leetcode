class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        xs = range(len(A))
        ys = range(len(A[0]))
        A_T = []
        for x in xs:
            row = []
            for y in ys:
                row.append(A[x][y]^0x1)
            A_T.append(row[::-1])
        return A_T
                