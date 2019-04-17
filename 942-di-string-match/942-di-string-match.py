class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        left = 0
        right = len(S)
        res = []
        for s in S:
            if s == 'I':
                res.append(left)
                left += 1
            else:
                res.append(right)
                right -= 1
        res.append(left)
        return res