#link : https://leetcode.com/problems/top-k-frequent-elements/description/

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapNums = {}
        heap = []
        for i in nums:
            if i in mapNums:
                mapNums[i] +=1
            else:
                mapNums[i] = 1
        
        for i in mapNums.keys():
            heapq.heappush(heap,(mapNums[i],i))
        ans = nlargest(k,heap)
        return [ans[i][1] for i in range(k)]
