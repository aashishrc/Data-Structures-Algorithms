class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ans = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[j] == target - nums[i]:
        #             return [i,j]
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                for j in range(i+1,len(nums)):
                    if nums[j] == target - nums[i]:
                        return [i,j]
        