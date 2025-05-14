class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1 
        m = (l + r)//2

        def binary_search(l, r, m):
            if l > r:
                return m + 1
            elif nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
                m = (l + r)//2
                return binary_search(l, r, m)
            else:
                r = m - 1
                m = (l + r)//2
                return binary_search(l, r, m)
        return binary_search(l,r,m)
                