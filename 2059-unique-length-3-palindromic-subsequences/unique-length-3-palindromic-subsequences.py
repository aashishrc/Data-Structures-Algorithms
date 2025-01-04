class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        uniq = set() #stores mid and outer char
        left = set()
        right = Counter(s)

        for m in s:
            right[m] -=1
            for c in left:
                if right[c] > 0:
                    uniq.add((m,c))
            left.add(m)
        return len(uniq)
        