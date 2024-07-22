class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        if total == (n*(n+1)/2):
            return 0
        else:
            return int((n*(n+1)/2) - total)