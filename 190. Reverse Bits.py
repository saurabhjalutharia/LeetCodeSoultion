import os
os.system("cls")
#----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def reverseNumerseBits(self, inputNumber) :
        reverseNum = 0
        while (inputNumber > 0) :                           #TRAVERSE/LOOP BITS FROM THE RIGHT SIDE 
            reverseNum = reverseNum << 1                    #APPLYING BITWISE LEFT SHIFT OPERATION ON REVERSE NUMBER BY 1
            if (inputNumber & 1 == 1) :                     #CUREENT BIT i.e. LAST BIT IS 1. TRUE.
                reverseNum = reverseNum ^ 1 
            inputNumber = inputNumber >> 1                  #APPLYING BITWISE RIGHT SHIFT OPERATION ON REVERSE NUMBER BY 1
        return reverseNum

query = 0b001011                                            #PASS THE NUMBER IN THE BINARY FORM BECAUSE LEADING ZERO IS NOT ALLOW IN PYTHON
object1 = Solution()
print(object1.reverseNumerseBits(query))
#----------------------------------------------------------------------------------------------------------------------------------------------------