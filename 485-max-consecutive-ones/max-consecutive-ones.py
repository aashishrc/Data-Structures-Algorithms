class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans, count = 0, 0
        for i in range(len(nums)):
            if nums[i]:
                count+=1
            else:
                ans = max(ans, count)
                count = 0
        ans = max(ans, count)
        return ans
