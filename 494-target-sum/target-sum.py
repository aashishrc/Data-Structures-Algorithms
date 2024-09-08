class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (total + target) % 2 != 0:
            return 0
        s1 = (total + target) // 2
        return self.countSubsetSum(nums, s1)

    def countSubsetSum(self, nums, target):
        n = len(nums)
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(target + 1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][target]