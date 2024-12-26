import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            counts[i] = 1 + counts.get(i,0)
        # print(counts)
        freq = sorted(counts.items(), key = lambda item:item[1], reverse=True)
        # print(freq)
        ans =[]
        for i in range(k):
            ans.append(freq[i][0])
        
        return ans