class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [0]
        for i in range(1, n + 1):
            res.append(res[i >> 1] + i % 2)
        return res
    # def countBits(self, n: int) -> List[int]:
    #     output = []
    #     for i in range(n+1):
    #         bi = bin(i)[2:]
    #         output.append(self.getBits(bi))
    #     return output
    
    # def getBits(self, s: str):
    #     count = 0
    #     for i in s:
    #         if i == "1":
    #             count +=1
    #     return count