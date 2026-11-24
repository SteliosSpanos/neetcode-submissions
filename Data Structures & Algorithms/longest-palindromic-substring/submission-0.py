class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] is true if the substring s[i..j] is a palindrome
        # A substring s[i..j] is a palindrome if s[i] == s[j] and dp[i+1][j-1] == true
        resIdx, resLen = 0, 0
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True

                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1
        return s[resIdx : resIdx + resLen]


        