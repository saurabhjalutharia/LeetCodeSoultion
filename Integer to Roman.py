import os
os.system("cls")
#--------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def intToRoman(self, number):
        intToRomDict = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
                        50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
        orderList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        list = []
        for x in orderList:
            if number != 0:
                remainingNum = number//x
                if remainingNum != 0:
                    for y in range(remainingNum):
                        list.append(intToRomDict[x])
                number = number % x
        return "".join(list)
x = 400
object1 = Solution()
print(object1.intToRoman(int(x)))