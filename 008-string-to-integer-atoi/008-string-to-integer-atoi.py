import sys

class Solution(object):
    @staticmethod
    def is_num(ch):
        return ord('0') <= ord(ch) <= ord('9')
    
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        if not s:
            return 0
        stack = []
        index = 0
        while index < len(s):
            if s[index] == ' ':
                index += 1
                continue
            else:
                break
        s = s[index:]
        #print(s)
        if s and (
            s[0] == '+' or
            s[0] == '-' or
            self.is_num(s[0])
        ):
            stack.append(s[0])
        else:
            return 0
        #print(stack)
        for i in range(1, len(s)):
            if self.is_num(s[i]):
                stack.append(s[i])
            else:
                break
        res = 0
        max_num = 2**31 - 1
        min_num = -2**31
        upper = 0
        while stack:
            c = stack.pop()
            if c == '+':
                break
            elif c == '-':
                res = -res
            else:
                res += int(c)*(10**upper)
                #print(res)
                upper += 1
        if res > max_num:
            return max_num
        if res < min_num:
            return min_num
        return res
            
            
                 
        