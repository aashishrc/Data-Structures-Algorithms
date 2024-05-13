class Solution:
    def findMin(self, nums: List[int]) -> int:
        #O(logn)
        n = len(nums)
        if n==1:
            return nums[0]
        min_val = float('inf')
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right)//2
            #identifying the sorted part
            if nums[left] <= nums[mid]:
                min_val = min(min_val, nums[left])
                left = mid + 1 #eliminating left half
            else:
                min_val = min(min_val, nums[mid])
                right = mid - 1 #eliminating right half

        #O(n)
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return nums[i + 1]
        return nums[0]