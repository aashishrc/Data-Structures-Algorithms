class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # top-down code
        def LCS(text1: str, text2: str, m, n):
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if text1[j-1] == text2[i-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            return dp[n][m]

        n = len(text2)
        m = len(text1)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)] # (n+1) cols x (m+1) rows
        for i in range(n+1):
            dp[i][0] = 0
        for j in range(m+1):
            dp[0][j] = 0
        return LCS(text1, text2, m, n)  

        #recursive + dp = memoization solution  
        # def LCS(text1: str, text2: str, m, n):
        #     if m == 0 or n == 0:
        #         return 0
        #     if dp[n][m] != -1:
        #         return dp[n][m]
        #     if text1[m-1] == text2[n-1]:
        #         dp[n][m] = 1 + LCS(text1, text2, m-1, n-1)
        #     else:
        #         dp[n][m] = max(LCS(text1, text2, m-1, n), LCS(text1, text2, m, n-1))
        #     return dp[n][m]

        # n = len(text2)
        # m = len(text1)
        # dp = [[-1 for _ in range(m+1)] for _ in range(n+1)] # (n+1) cols x (m+1) rows
        # return LCS(text1, text2, m, n)  