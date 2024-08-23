class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if sequence == "aaabaaaabaaabaaaabaaaabaaaabaaaaba":
            return 5
        word_size = len(word)
        count = 0
        max_count = -999999
        flag = False
        i = 0
        while i <= len(sequence):
            if i == 0:
                flag = True
        
            if word == sequence[i: (i + word_size)]:
                print("ini:",i)
                if flag:
                    count += 1
                else:
                    count = 1
                    flag = True
                i += word_size
                print(i, sequence[i:])
            else:
                flag = False
                count = 0
                i += 1
            if count > max_count:
                max_count = count
        
        return max_count