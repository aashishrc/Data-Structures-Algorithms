class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        steps = nums[0]
        for i in range(n):
            if steps >= 0 :
                if i == len(nums) - 1 :
                    return True
                if nums[i] <= steps:
                    steps -=1
                elif nums[i] > steps and steps >= 0:
                    steps = nums[i] -1
            elif steps < 0:
               return False
        if steps >= 0:
            return True