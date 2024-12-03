class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
        
            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -=1
                l +=1
            res = max(res, r - l + 1)
        return res
        # count = 0
        
        # for i in range(len(s)):
        #     temp = k
        #     t_count = 1
        #     for j in range(i+1, len(s)):
        #         if s[i] == s[j]:
        #             t_count +=1
        #             continue
        #         elif temp > 0:
        #             temp -=1
        #             t_count += 1
        #         else:
        #             break
        #     if temp > 0 and t_count < len(s):
        #         for i in range(temp):
        #             if t_count == len(s):
        #                 break
        #             elif t_count < len(s):
        #                 t_count += 1
        #     count = max(count, t_count)
        # return count