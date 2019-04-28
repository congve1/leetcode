class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        res = 0
        for num in range(L, R+1):
            temp = num
            count = 0
            while temp:
                temp = temp & (temp-1)
                count += 1
            if count in primes:
                res += 1
        return res