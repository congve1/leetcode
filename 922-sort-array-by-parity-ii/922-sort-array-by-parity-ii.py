class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        res = [0 for _ in range(len(A))]
        even = 0
        odd = 1
        for num in A:
            if num % 2 == 0:
                res[even] = num
                even += 2
            if num % 2 == 1:
                res[odd] = num
                odd += 2
                
        return res