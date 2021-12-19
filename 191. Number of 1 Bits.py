import os
os.system("cls")
#----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def hammingWeight(self, inputNumber):   
        OneCounter = 0                              #COUNTER VARIABLE TO COUNT NUMBER OF ONES
        while(True):                                #LOOP TILL NUMBER NOT BECOME ZERO
            if inputNumber == 0:                    #BREAK IF USER ENTER NOTHING
                break
            if inputNumber & 1 == 1:                #TO CHECK WHEATHER THE LAST NUMBER IS 1 OR NOT
                OneCounter += 1                     #IF ONE INCREMENT THE COUNTER VALUE BY 1
            inputNumber = int(inputNumber / 2)      #DIVIDE NUMBER BY 2 SO THAT LAST VALUE GET REMOVE FROM THE NUMBER
        return OneCounter   
#----------------------------------------------------------------------------------------------------------------------------------------------------
query = 0b001011                                    #PASS THE NUMBER IN THE BINARY FORM BECAUSE LEADING ZERO IS NOT ALLOW IN PYTHON
object1 = Solution()
print(object1.hammingWeight(query))
#----------------------------------------------------------------------------------------------------------------------------------------------------
