class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        prev2, prev1 = 1, 1  # Equivalent to dp[i-2] and dp[i-1]

        for i in range(1, n):
            current = 0
            if s[i] != '0':
                current += prev1
            if 10 <= int(s[i-1:i+1]) <= 26:
                current += prev2
            prev2, prev1 = prev1, current

        return prev1


    # def numDecodings(self, s: str) -> int:
    #     if s[0] == '0':
    #         return 0
    #     # h = {}
    #     # ascii_val = 65
    #     # for i in range(26):
    #     #     # print(ascii_val)
    #     #     h[i + 1] = chr(ascii_val)
    #     #     ascii_val += 1
    #     n = len(s)
    #     i = n -1
    #     nums = []
    #     while i >= 0:
    #         if s[i] == '0':
    #             if s[i-1] == '0':
    #                 return 0
    #             else:
    #                 nums.append(s[i-1:i+1])
    #                 i -=1
    #         else:
    #             nums.append(s[i])
    #         i -=1
    #     nums.reverse()
    #     print(nums)
    #     main = set()
    #     n = len(nums)
    #     dp = [1]*(n+1)
    #     def func(start, dp):
    #         print("inside: ", start, dp)
    #         if start > n-1:
    #             return 0
    #         if dp[start] > 1:
    #             return dp[start]
    #         if int(nums[start] + nums[start-1]) <= 26:
    #             dp[start] = dp[start-1] + func(start + 1, dp)
    #         else:
    #             dp[start] =func(start + 1, dp)
    #         print("dp: ", dp, " start: ", start )
    #         return dp[start]
    #     ans = func(0, dp)
    #     # print(dp)
    #     return ans
             
        # print(main)
                

        
            
