class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            s1 = words[i]
            for j in range(i+1, len(words)):
                s2 = words[j]
                if len(s1) > len(s2):
                    pass
                # print(s1,s2[:len(s1)], s2[-len(s1):])
                if s1 == s2[:len(s1)] and s1 == s2[-len(s1):]:
                    count +=1
        return count