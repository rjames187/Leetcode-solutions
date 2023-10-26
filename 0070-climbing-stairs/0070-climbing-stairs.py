class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(steps):
            if steps == n:
                return 1
            if steps > n:
                return 0
            if steps in memo:
                return memo[steps]
            res = helper(steps + 1) + helper(steps + 2)
            memo[steps] = res
            return res
        return helper(0)
            
            