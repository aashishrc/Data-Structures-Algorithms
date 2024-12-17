class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[resIdx : resIdx + resLen]
                
        #bruteforce        
        # ans = s[0]
        # for i in range(len(s)):
        #     for j in range(len(s) - 1, -1, -1):
        #         if s[i] == s[j]:
        #             k = i
        #             l = j
        #             while l >= k and s[l] == s[k]:
        #                 k +=1
        #                 l -=1
        #             if l > k:
        #                 continue
        #             else:
        #                 if j - i + 1 > len(ans):
        #                     # print(i, j)
        #                     ans = s[i:j+1]  
        #                 break
        # return ans