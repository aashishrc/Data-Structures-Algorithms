class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #optimized
        char_set = set()  # A set to store characters in the current substring
        n = len(s)
        i = 0  # Left pointer of the sliding window
        max_length = 0  # Maximum length of the substring

        for j in range(n):  # `j` is the right pointer of the sliding window
            while s[j] in char_set:  # If duplicate is found, slide the left pointer
                char_set.remove(s[i])
                i += 1
            char_set.add(s[j])  # Add the current character to the set
            max_length = max(max_length, j - i + 1)  # Update max length

        return max_length

        # se = set()
        # i = 0
        # n = len(s)
        # count = 0
        # j = i
        # while i <= n -1:
        #     if s[i] in se:
        #         count = max(count, len(se))
        #         se.clear()
        #         i = j+1
        #         j +=1
        #     if s[i] not in se:
        #         se.add(s[i])
        #         i +=1
        # count = max(count,len(se))
        # return count
            
