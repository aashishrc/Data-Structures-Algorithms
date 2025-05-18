class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        count = 0
        j = 0
        for i in range(0, len(g)):
            if j < len(s) and g[i] <= s[j]:
                count +=1
                j+=1
        return count