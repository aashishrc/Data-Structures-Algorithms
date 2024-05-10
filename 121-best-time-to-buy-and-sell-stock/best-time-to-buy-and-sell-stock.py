class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = prices[0]
        # m = {}
        # for i in range(len(prices)):
        #     m[i + 1] = prices[i]
        # m = sorted(m.items(), key=lambda i: i[1])
        # for i in range(len(m)):
        #     a, b = m[i]
        #     for j in range(len(m)-1, i, -1):
        #         k, v = m[j]
        #         if k > a:
        #             if v - b > profit:
        #                 profit = v - b
             
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         if prices[j] > prices[i] and prices[j] - prices[i] > profit:
        #             profit = prices[j] - prices[i]

        for i in range(1, len(prices)):
            cost = prices[i] - mini
            profit = max(cost, profit)
            mini = min(mini, prices[i])
        return profit
        