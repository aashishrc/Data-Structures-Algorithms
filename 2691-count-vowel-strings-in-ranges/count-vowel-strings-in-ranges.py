class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a','e','i','o','u']
        vow_score = []
        ans = []
        pre_vow = 0
        for i in words:
            if i[0] in ['a','e','i','o','u'] and i[-1] in ['a','e','i','o','u']:
                vow_score.append(1)
            else:
                vow_score.append(0)
        for i in range(len(vow_score)):
            pre_vow += vow_score[i]
            vow_score[i] = pre_vow
        for q in queries:
            l,r = q[0], q[1]
            if l == 0:
                ans.append(vow_score[r])
            else:
                ans.append(vow_score[r] - vow_score[l-1])
        return ans