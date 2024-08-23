class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        word_size = len(word)
        count = 0
        max_count = -999999
        dp = [0]*(len(sequence)+1 )
        flag = False
        for i in range(len(sequence)):
            if word == sequence[i: (i + word_size)]:
                count = 0
                j = i
                while j < len(sequence):
                    if word == sequence[j: (j + word_size)]:
                        # print("ini:",i)
                        count += 1
                        # print("incremented count for j : ", j, "and count : ", count)
                        j += word_size
                        # print(j, sequence[j:])
                    else:
                        break
                dp[i] = count
        # print(dp)
        return max(dp)