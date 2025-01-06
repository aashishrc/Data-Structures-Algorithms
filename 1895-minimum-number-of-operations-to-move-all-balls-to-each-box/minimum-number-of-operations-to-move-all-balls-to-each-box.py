class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        c = []
        for i in range(len(boxes)):
            if boxes[i] == '1':
                c.append(i)
        ans = []
        print(c)
        for i in range(len(boxes)):
            tot = 0
            for j in c:
                tot += abs(i-j)
            ans.append(tot)
        return ans
        