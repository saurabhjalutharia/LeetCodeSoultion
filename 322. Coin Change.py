import os
os.system("cls")
#----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution():
    def coinChange(self, coins, amount):
        sortedCoins = sorted(coins)
        dp = [amount for i in range(amount+1)]
        dp[0] = 0
        for eachAmount in range(1, amount+1):
            for coin in sortedCoins:
                if coin <= eachAmount:
                    dp[eachAmount] = min(dp[eachAmount], 1+dp[eachAmount-coin])
                else:
                    break
        return dp[amount] if dp[amount]<=amount else -1

coins = [2]
amount = 3
object1 = Solution()
print(object1.coinChange(coins, amount))
#----------------------------------------------------------------------------------------------------------------------------------------------------