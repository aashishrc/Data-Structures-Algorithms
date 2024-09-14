class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # A large value greater than the maximum possible number of coins required, even infinity is fine
        max_value = float('inf')
        n = len(coins)
        
        dp = [[0 for _ in range(amount+1)] for _ in range(n +1 )]
        
        for i in range(amount + 1):
            dp[0][i] = max_value
        for i in range(1, n+1):
            dp[i][0] = 0

        for i in range(1, amount +1):
            if i % coins[0] == 0:
                dp[1][i] = i// coins[0]
            else:
                dp[1][i] = max_value
        
        for i in range(2, n +1):
            for j in range(1, amount + 1):
                if coins[i-1] <= j:
                    dp[i][j] = min(dp[i-1][j], 1 + dp[i][ j - coins[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]

        # print(dp)
        return dp[n][amount] if dp[n][amount] != float('inf') else -1


    #    # Initialize dp array where dp[i] represents the minimum number of coins needed for amount i
    #    # dp[i] is initialized with max_value, which is essentially infinity
    #    dp = [max_value] * (amount + 1)
       
    #    # Base case: No coins are needed to make the amount 0
    #    dp[0] = 0
       
    #    # Iterate through each coin denomination
    #    for coin in coins:
    #        # Iterate through all amounts from the current coin value to the target amount
    #        for x in range(coin, amount + 1):
    #            # Update dp[x] with the minimum of:
    #            # 1. The current value of dp[x] (minimum coins needed without considering the current coin)
    #            # 2. dp[x - coin] + 1 (minimum coins needed for the remaining amount (x - coin) plus the current coin)
    #            dp[x] = min(dp[x], dp[x - coin] + 1)
       
    #    # If dp[amount] is still max_value, it means the target amount cannot be made up by any combination of the coins
    #    # In that case, return -1 to indicate that it's not possible to make the change
    #    # Otherwise, return dp[amount], which represents the minimum number of coins needed
    #    return dp[amount] if dp[amount] != max_value else -1