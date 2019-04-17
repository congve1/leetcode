class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right+1):
            temp = num
            #is_self_divide = True
            while temp:
                residual = temp % 10
                if not residual:
                    #is_self_divide = False
                    break
                if num % residual != 0:
                    #is_self_divide = False
                    break
                temp = temp // 10

            if not temp:
                res.append(num)
        return res
            
                