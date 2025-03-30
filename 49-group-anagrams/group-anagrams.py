class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorts = {}
        for i in strs:
            k = "".join(sorted(i))
            if k not in sorts.keys():
                sorts[k] = []
            sorts[k].append(i) 
        ans = []
        # print(sorts)
        for k,v in sorts.items():
            ans.append(v)
        return ans