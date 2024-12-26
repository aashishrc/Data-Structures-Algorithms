class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {}
        dist = []
        counter = 0
        for i in points:
            x,y = i
            # print(x,y)
            d = math.sqrt((x)**2 + (y)**2)
            # print(d)
            counter +=1
            heapq.heappush(dist, (d,counter,i))
        ans = [i[2] for i in heapq.nsmallest(k,dist)]
        # print(ans)
        return ans