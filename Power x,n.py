import os
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x

        result = self.myPow(x, n // 2)					#RECURSIVE CALLING
        return result * result * (x if n % 2 else 1)	
#---------------------------------------------------------------------------------------------------------------------------------------
x = 7
y = 3
obj = Solution()
print(obj.myPow(x, y))