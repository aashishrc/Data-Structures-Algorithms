class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)): return False
        windows = set()
        for i in range(len(nums)):
            if nums[i] in windows:
                return True
            windows.add(nums[i])

            if len(windows) > k:
                windows.remove(nums[i - k])
        return False

# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         d ={}
#         for i in range(len(nums)):
#             if nums[i] in d:
#                 if abs(d[nums[i]][-1] - i) <= k:
#                     return True
#                 else:
#                     d[nums[i]].append(i)
#             else:
#                 d[nums[i]] = [i]
#         return False
