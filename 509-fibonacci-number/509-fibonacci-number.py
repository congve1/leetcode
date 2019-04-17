class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        def my_fib(n, a, b):
            if n == 0:
                return 0
            if n == 1:
                return b
            return my_fib(n-1, b, a+b)
        return my_fib(N, 0, 1)
        