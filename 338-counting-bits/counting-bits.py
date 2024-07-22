class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            bi = bin(i)[2:]
            output.append(self.getBits(bi))
        return output
    
    def getBits(self, s: str):
        count = 0
        for i in s:
            if i == "1":
                count +=1
        return count