class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1]
        ans = []
        for i in range(len(nums) - 1):
            pre.append(pre[i]*nums[i])
        for i in range(len(nums) - 1, 0, -1):
            post.insert(0,post[0]*nums[i])
        for i in range(len(nums)):
            ans.append(pre[i]*post[i])
        return ans