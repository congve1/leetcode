import sys
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        int_max = 2**31 - 1
        int_min = -2**31
        is_negative = x < 0
        if is_negative:
            x = -x
        while x != 0:
            pop = x % 10
            x = int(x/10)
            if (rev > int_max/10) or (rev == int(int_max/10) and pop > 7):
                return 0
            if (rev < int_min/10) or (rev == int(int_min/10) and pop < -8):
                return 0
            rev = rev*10 + pop
        if is_negative:
            rev = -rev
        return rev
        