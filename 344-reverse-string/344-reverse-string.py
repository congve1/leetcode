class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
        mid = len(s)//2
        len_s = len(s)
        for i in range(mid):
            temp = s[i]
            s[i] = s[len_s-i-1]
            s[len_s-i-1] = temp
        """
        left = 0
        right = len(s) - 1
        while left <= right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        