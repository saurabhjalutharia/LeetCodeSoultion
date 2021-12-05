import os
os.system("cls")

class Solution:
    def addBinary(self, a, b):
        result = ""
        aCount = len(a) - 1
        bCount = len(b) - 1
        carry = 0
        while aCount >= 0 or bCount >= 0:
            totalSum = carry
            if aCount >= 0:
                totalSum += int(a[aCount])
                aCount -= 1
            if bCount >= 0:
                totalSum += int(b[bCount])
                bCount -= 1
    
            result = str(totalSum % 2) + result     #ADD BITs IN THE RESULT
            carry = totalSum // 2                   #UPDATE CARRY

        if carry > 0:                               #CHECK WHEATHER CARRY EXISTS OR NOT
            result = str(1) + result
        return result

anum = "101"
bnum = "11"
obj = Solution
print(Solution.addBinary(obj,anum,bnum))        