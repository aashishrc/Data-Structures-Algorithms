class Solution:
    def maxScore(self, s: str) -> int:
        zeroes = []
        count = 0
        for i in range(len(s)):
            if s[i] == '0':
                count +=1
            zeroes.append(count)
        tot = zeroes[-1]
        n = len(s)
        score = 0
        for i in range(len(s)-1):
            left = zeroes[i]
            rem = tot - left
            ones = n - rem - (i+1)
            score = max(score,left+ones)
        return score
