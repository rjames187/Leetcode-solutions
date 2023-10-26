memo = {}

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        if n in memo:
            return memo[n]
        res = self.fib(n - 1) + self.fib(n - 2)
        memo[n] = res
        return res
            
            
        