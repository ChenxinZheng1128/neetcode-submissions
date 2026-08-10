class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[a] stores the number of ways to make amount 'a'
        dp = [0] * (amount + 1)
        dp[0] = 1  # Base case: 1 way to make amount 0

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]

        return dp[amount]