class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = ''.join(sorted(s))
        # t = ''.join(sorted(t))
        if len(t) != len(s):
            return False
        hash = {}
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i]+=1
        # print(hash)
        for i in t:
            if i in hash:
                hash[i] -=1
            else:
                return False
        # print(hash)
        for i,v in hash.items():
            if v > 0:
                return False
        return True