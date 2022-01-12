import os
os.system("cls")
#----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution(object):
    def findNthDigit(self, userInput):
        digitCounter = 1
        numberCount = 9
        while userInput > digitCounter * numberCount:
            userInput -= digitCounter * numberCount
            digitCounter += 1
            numberCount *= 10
 
        userInput -= 1                              
        quotient = userInput / digitCounter
        remainder = userInput % digitCounter
        target = numberCount / 9 + quotient
        return int(str(target)[remainder])
#----------------------------------------------------------------------------------------------------------------------------------------------------
query = 2
object1 = Solution()
print(object1.findNthDigit(query))
#----------------------------------------------------------------------------------------------------------------------------------------------------