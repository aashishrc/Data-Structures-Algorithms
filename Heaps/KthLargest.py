#link: https://leetcode.com/problems/kth-largest-element-in-an-array/description/

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heap.append(-nums[i])
        heapq.heapify(heap)
        for i in range(k - 1):
            heapq.heappop(heap)
        return -1*heappop(heap)