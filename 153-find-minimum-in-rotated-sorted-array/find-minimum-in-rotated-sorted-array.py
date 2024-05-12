class Solution:
    def findMin(self, nums: List[int]) -> int:
        #O(logn)
        n = len(nums)
        if n==1:
            return nums[0]
        min_val = float('inf')
        left = 0
        right = n-1
        while left<=right:
            if nums[left]<=nums[right]:
                min_val = min(nums[left],min_val)
                break
                #left half has smallest elem
            else:
                mid = (left+right)//2
                min_val = min(nums[mid],min_val)
                if nums[left]<=nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
                #right half has smallest elem
        return min_val


        #O(n)
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return nums[i + 1]
        return nums[0]