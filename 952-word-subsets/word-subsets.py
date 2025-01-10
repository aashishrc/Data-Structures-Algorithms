class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []
        flag = 0
        main = {}
        w2 = [ 0 for i in range(26)]
        for w in words2:
            wc = Counter(w)
            for i,j in wc.items():
                k = ord(i) - ord('a')
                if j > w2[k]:
                    w2[k] = j
        for w in words1:
            t = Counter(w)
            flag = 0
            for i in range(len(w2)):
                if w2[i] != 0:
                    c = chr(ord('a') + i)
                    if c not in t or t[c] < w2[i]:
                        flag = 1
                        break
            if not flag:
                ans.append(w)
                    
        return ans
            