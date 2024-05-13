class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            # print("begin:", low, high)
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            else:
                #identifying sorted array
                if nums[low] <= nums[mid]:
                    #left half
                    if target >= nums[low] and target <= nums[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] <= nums[high]:
                    #right half
                    if target >= nums[mid] and target <= nums[high]:
                        low = mid + 1
                    else:
                        high = mid - 1
            # print("right:", low, high)
        return -1



