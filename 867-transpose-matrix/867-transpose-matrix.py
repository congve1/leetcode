class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        row_T = len(A[0])
        col_T = len(A)
        A_T = [[0 for j in range(col_T)] for i in range(row_T)]
        for i in range(row_T):
            for j in range(col_T):
                A_T[i][j] = A[j][i]
        return A_T
        """
        return list(zip(*A))

                
        