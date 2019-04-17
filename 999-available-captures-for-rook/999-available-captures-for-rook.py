class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        cnt = 0
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rook = [(i, j) for i in range(8) for j in range(8) if board[i][j] == 'R']
        ii, jj = rook[0][0], rook[0][1]
        #print(ii)
        for move in moves:
            #print(move[0])
            i, j = ii, jj
            while True:
                i = i + move[0]
                j = j + move[1]
                if i > 7 or i < 0:
                    break
                if j > 7 or j < 0:
                    break
                #print(i, j)
                if board[i][j] == 'B':
                    break
                if board[i][j] == 'p':
                    cnt += 1
                    break
        return cnt
                
        