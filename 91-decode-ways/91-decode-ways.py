class Solution:
    def numDecodings(self, s: str) -> int:
        """ Return for string s the number of ways to decode. """
        
        
        #utility function
        def is_valid(num):
            if len(num) == 2 and num[0] == '0':
                return False
            return 0 < int(num) < 27
        
        #initialize dp array
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1 if is_valid(s[0]) else 0
        
        #edge case
        if len(s) == 1:
            return dp[1]
        
        for n in range(2, len(s) + 1):
            # if first digit is valid
            dp[n] += dp[n - 1] if is_valid(s[n - 1]) else 0
            # if first two digits are valid
            dp[n] += dp[n - 2] if is_valid(s[n - 2 : n]) else 0
            
        return dp[len(s)]
        
        
        
        
        
        