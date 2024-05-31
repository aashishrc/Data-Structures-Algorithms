class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #code to see if two tripplets are diferent
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue
            j = i + 1
            k = n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j +=1
                elif sum > 0:
                    k -=1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)
                    j +=1
                    k -=1
                    while k + 1 < n and j < k and nums[k] == nums[k+1]:
                        k -=1
                    while j < k and nums[j] == nums[j-1]:
                        j +=1
        return ans
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if i == j:
        #             continue
        #         for k in range(n):
        #             if j == k or i==k:
        #                 continue
        #             sum = nums[i] + nums[j] + nums[k]
        #             if not sum:
        #                 l = [nums[i],nums[j],nums[k]]
        #                 l.sort()
        #                 if l not in ans:
        #                     ans.append(l)
        # return ans
        