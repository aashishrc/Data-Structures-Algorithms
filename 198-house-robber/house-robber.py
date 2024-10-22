# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         s = 0
#         def fun(i,s):
#             if i >= n:
#                 return s
#             elif i == n-1:
#                 return nums[i] + s
#             return max(fun(i+2, s + nums[i]), fun(i+3, s + nums[i+1]))
        
#         return fun(0,s)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def fun(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]

            # Either rob the current house and skip the next one or skip this house
            memo[i] = max(nums[i] + fun(i + 2), fun(i + 1))
            return memo[i]
        
        return fun(0)
