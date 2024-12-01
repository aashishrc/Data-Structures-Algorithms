class Solution:
    def climbStairs(self, n: int) -> int:
        if n<= 2:
            return n
        dp = [-1]*(n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
    #     if n <= 2:
    #         return n
    #     else:
    #         tp = n //2
    #         counter = 0
    #         #add 1 way at the end when there are 0 2's and all 1's
    #         for i in range(1, tp + 1):
    #             op = n - i*2
    #             #code to find all possibilities
    #             counter += self.calc_poss(op + i, op, i)
    #         return counter + 1

    # def calc_poss(self, tot_places, op, tp):
    #     return self.factorial(tot_places)//(self.factorial(op)*self.factorial(tp)) 

    # def factorial(self,n):
    #     # single line to find factorial
    #     return 1 if (n==1 or n==0) else n * factorial(n - 1) 