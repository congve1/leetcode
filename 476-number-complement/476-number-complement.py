import math
class Solution:
    def findComplement(self, num: int) -> int:
        """
        bits = int(math.floor(math.log2(num)))
        x = 0x00000001
        for i in range(1, bits+1):
            temp = 0x00000001 << i
            x = temp + x
        return num^x
        """
        n = num
        xor = 1
        while n > 0:
            num = num ^ xor
            xor = xor << 1
            n = n >> 1
        return num
        