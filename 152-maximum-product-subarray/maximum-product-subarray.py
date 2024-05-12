class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = -99999
        prefix = 0
        suffix = 0
        # Bruteforce : works for 187/190 cases
        # for i in range(len(nums)):
        #     prod = nums[i]
        #     for j in range(i+1,len(nums)):
        #         prod = prod*nums[j]
        #         max_prod = max(prod, max_prod)
        #     max_prod = max(prod, nums[i], max_prod)
        # return max_prod

        # using dp
        for i in range(len(nums)):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix =1
            prefix *= nums[i]
            suffix *= nums[len(nums) - i - 1]
            max_prod = max(max_prod, max(prefix, suffix))
        return max_prod