class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def LCS(text1: str, text2: str, m, n):
            if m == 0 or n == 0:
                return 0
            if dp[n][m] != -1:
                return dp[n][m]
            if text1[m-1] == text2[n-1]:
                dp[n][m] = 1 + LCS(text1, text2, m-1, n-1)
            else:
                dp[n][m] = max(LCS(text1, text2, m-1, n), LCS(text1, text2, m, n-1))
            return dp[n][m]

        n = len(text2)
        m = len(text1)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)] # (n+1) cols x (m+1) rows
        return LCS(text1, text2, m, n)    