class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxi = nums[0]
        for i in nums:
            sum += i
            if sum > maxi:
                maxi = sum
            if sum < 0:
                sum = 0
        return maxi