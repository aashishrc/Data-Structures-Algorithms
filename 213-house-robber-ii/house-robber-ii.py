class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        # Helper function to calculate max loot for a range of houses
        def rob_range(start, end):
            prev2, prev1 = 0, 0  # Equivalent to dp[i-2] and dp[i-1]
            for i in range(start, end + 1):
                current = max(prev1, prev2 + nums[i])
                prev2, prev1 = prev1, current
            return prev1
        
        # Case 1: Exclude the last house (0 to n-2)
        # Case 2: Exclude the first house (1 to n-1)
        return max(rob_range(0, n - 2), rob_range(1, n - 1))
        # n = len(nums)
        # s = 0
        # flag = 0
        # if n == 3:
        #     return max(nums)
        # dp = [[0] * (n + 1) for _ in range(2)]
        # # print(dp)
        # def fun(i,s,flag):
        #     if i >= n:
        #         return 0
        #     if dp[flag][i]:
        #         return dp[flag][i]
        #     if i == n-1:
        #         if flag:
        #             return dp[flag][i]
        #         return nums[i]
            
        #     if i == 0:
        #         flag = 1
        #         dp[flag][i] += max((nums[i] + fun(i+2,s, flag) ), fun(i+1,s, 0))
        #     else:
        #         dp[flag][i] += max((nums[i] + fun(i+2,s, flag)), fun(i+1,s, flag))
        #     return dp[flag][i]
        # # def fun(i,s,flag):
        # #     if i >= n:
        # #         return 0
        # #     elif i == n-1:
        # #         if flag:
        # #             return 0 
        # #         return nums[i]
        # #     if i == 0:
        # #         flag = 1
        # #         s += max((nums[i] + fun(i+2,s, flag) ), fun(i+1,s, 0))
        # #     else:
        # #         s += max((nums[i] + fun(i+2,s, flag)), fun(i+1,s, flag))
        # #     return s
        
        # return fun(0,s,flag)    