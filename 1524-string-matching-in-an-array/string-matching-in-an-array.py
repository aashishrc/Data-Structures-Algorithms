class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for i in words:
            for j in words:
                if i !=j and i in j:
                    ans.add(i)
        return list(ans)