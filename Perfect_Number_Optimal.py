import os
os.system("cls")

from math import sqrt
class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        sums = 1
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                sums += i + num // i
        return sums == num
query = 33550336
obj = Solution
print(Solution.checkPerfectNumber(obj, query))