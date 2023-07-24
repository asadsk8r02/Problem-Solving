class Solution:
    def fib(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)

        # a, b = 0, 1
        # for i in range(n):
        #     a, b = b, a + b
        # return a