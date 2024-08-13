class Solution:
    def fib(self, n: int) -> int:
        fib = []
        fib.append(0)
        fib.append(1)
        if n == 0:
            return 0
        elif n ==1:
            return 1    
        else:
            # print(fib)
            for i in range(2, n +1):
                fib.append(fib[-2] + fib[-1])
        return fib[n] 
        
        
        
        #recursive
        # if n == 0:
        #     return 0
        # elif n ==1:
        #     return 1
        # return self.fib(n-1) + self.fib(n-2)