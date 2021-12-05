import os
os.system("cls")

class Solution:
    def checkPerfectNumber(self, num):
        if num < 0:
            return False
        a = [i for i in range(1, num) if (num%i)==0]
        if sum(a)==num:
            return True
        else:
            return False
query = 8128
obj = Solution
print(Solution.checkPerfectNumber(obj, query))