class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squares = [a**2 for a in A]
        return sorted(squares)
        