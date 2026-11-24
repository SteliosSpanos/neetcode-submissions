class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] is the distinct number of ways to reach stair i
        
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
        