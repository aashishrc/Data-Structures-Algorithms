class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pre = []
        s = 0
        ans = 0
        for i in range(len(nums)):
            s += nums[i]
            pre.append(s)
        for i in range(len(pre)-1):
            if pre[i] >= pre[-1] - pre[i]:
                ans +=1
        return ans