class Solution:
    def reorganizeString(self, s: str) -> str:
        # """
        # aab -> baa aba aab

        # aabbcdef -> ababcdef a: 2 b: 2 c: 1 d:1 f:1
        # _ _ _ _ _ _ _ _
        # a c a d b e b f

        # 1. get counts of each char
        # 2. place characters with a jump of 2 starting from highest freq
        #-> go out of bounds start from index 1
        # 3. at index 1 if index 0 is same -> return ""

        # aaab a:3 b:1
        # _ _ _ _
        # a a  a

        # 

        # """
        n = len(s)
        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1
        
        highest_freq_char = None
        for char, count in counts.items():
            if highest_freq_char is None or count > counts[highest_freq_char]:
                highest_freq_char = char
        
        index = 0
        out = ["" for _ in range(n)] # output character list 

        while counts[highest_freq_char] > 0:
            if index >= n: 
                return ""
            out[index] = highest_freq_char

            # update for next iteration
            index += 2
            counts[highest_freq_char] -= 1

        del counts[highest_freq_char] # remove from the map
        
        # place rest of the characters in the string
        for char in counts:
            while counts[char] > 0:
                if index >= n: index = 1
                out[index] = char
                
                counts[char] -= 1
                index += 2
        
        return "".join(out)


        

        




       


        