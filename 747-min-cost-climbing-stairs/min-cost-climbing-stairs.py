class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # if len(cost) <= 2:
        #     return 0
        total_cost = 0
        target = len(cost) - 1
        i = target
        dp = [0]*(target +1)
        for i in range(target, -1, -1):
            if i == target - 1 or i == target:
                dp[i] = cost[i]
            else:
                if dp[i+1] > dp[i+2]:
                    dp[i] = cost[i] + dp[i+2]
                else:
                    dp[i] = cost[i] + dp[i+1]
            # print(dp)
        if dp[i] < dp[i+1]:
            return dp[i]
        return dp[i+1]
            

            
        