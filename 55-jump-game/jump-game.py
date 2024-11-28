class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        end = len(nums) - 1
        steps = nums[0]
        for i in range(n):
            if i == end and steps >= 0 :
                return True
            elif steps < 0:
                return False
            print(i, " : steps : ", steps)
            if nums[i] <= steps:
                steps -=1
            elif nums[i] > steps and steps >= 0:
                steps = nums[i] -1
        if steps >= 0:
            return True
            # if nums[i] > end - i: 
            #     nums[i] = end - i
        # print(nums)
        # dp = [False]*(end+2)
        # def func(start):
        #     print(start)
        #     if start > end:
        #         dp[start] = False
        #         return dp[start]
        #     if start == end:
        #         dp[start] = True
        #         return dp[start]
        #     if dp[start]:
        #         return dp[start]
        #     if nums[start]:
        #         for i in range(nums[start], -1, -1):
        #             dp[start] =  func(start+i) 
        #             if dp[start]:
        #                 break
        #         return dp[start]
        #     else:
        #         dp[start] = False
        #         return dp[start]
        # return func(0)