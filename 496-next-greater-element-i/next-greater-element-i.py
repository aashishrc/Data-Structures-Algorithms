class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if j == len(nums2) -1:
                        ans.append(-1)
                    else:
                        f = 0
                        for k in range(j+1, len(nums2)):
                            if nums2[k] > nums1[i]:
                                ans.append(nums2[k])
                                f = 1
                                break
                        if not f:
                            ans.append(-1)
                            break
        return ans