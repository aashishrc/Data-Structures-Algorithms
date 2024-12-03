class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()
        i = 0
        n = len(s)
        count = 0
        j = i
        while i <= n -1:
            if s[i] in se:
                count = max(count, len(se))
                se.clear()
                i = j+1
                j +=1
            if s[i] not in se:
                se.add(s[i])
                i +=1
        count = max(count,len(se))
        return count
            
