class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1]*len(nums)
        n = len(nums) - 1
        for i in range(n, -1, -1):
            for j in range(i+1, n+1):
                if nums[i] < nums[j]:   
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)