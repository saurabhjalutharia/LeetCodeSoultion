import os
os.system("cls")
#----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def isPowerOfTwo(self, inputNumber):
        if inputNumber < 0:                         #TAKE ONLY POSITIVE INPUT ONLY
            return False 
        elif bin(inputNumber).count('1') == 1:      #CONVERT THE INPUT NUMBER INTO BINARY FORM AND COUNT THE NUMBER OF 1's IN IT
            return True                             #IF NUMBER OF 1's IS ONLY ONE MEANS THE INPUT IS A VALID POWER OF 2 AND RETURN TRUE
        else:                                       #IN BINARY FORM 1 APPEAR ONLY ONCES IN 2,4,8,16,32... ELSE 1 APPEAR ATLEAST ONCES
            return False
#----------------------------------------------------------------------------------------------------------------------------------------------------
query = -16
object1 = Solution()
print(object1.isPowerOfTwo(query))
#----------------------------------------------------------------------------------------------------------------------------------------------------