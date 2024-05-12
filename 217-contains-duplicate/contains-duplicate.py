class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for i in nums:
            if i in m.keys():
                return True
            else:
                m[i] = 1
        return False

                # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False


        