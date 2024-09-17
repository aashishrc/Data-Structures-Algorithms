class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def func(st):
            ans = False
            if st in cache:
                return cache[st]
            if st == "":
                return True
            for w in wordDict:
                if w == st[:len(w)]:
                    ans = func(st[len(w):])
                if ans:
                    break
            cache[st] = ans
            return ans
        
        return func(s)

        