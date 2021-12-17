import os, math
os.system("cls")
#----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def numSquares(self, inputNumber):
        squareNumList = [i**2 for i in range(0, int(math.sqrt(inputNumber)) + 1)]
        dp = [float('inf')] * (inputNumber + 1)
        dp[0] = 0
        for i in range(1, inputNumber + 1):
            for square in squareNumList:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[inputNumber]

query = 5
object1 = Solution()
print(object1.numSquares(query))