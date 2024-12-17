class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        for i in range(len(s)):
            for j in range(len(s) - 1, -1, -1):
                if s[i] == s[j]:
                    k = i
                    l = j
                    while l >= k and s[l] == s[k]:
                        k +=1
                        l -=1
                    if l > k:
                        continue
                    else:
                        if j - i + 1 > len(ans):
                            print(i, j)
                            ans = s[i:j+1]  
                        break
        return ans