import os
os.system("cls")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def grayCode(self, inputNumber):
        resultList = [0]                                        #FINAL LIST THAT RETURN.DEFAULT FIRST VALUE IS ZERO

        for i in range(inputNumber):
            for j in range(len(resultList) - 1, -1, -1):        #LOOP FROM LAST TO FIRST AND DECREMENT EACH STEP BY ONE
                resultList.append(resultList[j] | 1 << i)       #ADD(ORing) RESULT LIST POISITION VALUE OF j WITH THE LEFT SHIT OPERATION ON 1
        return resultList
#------------------------------------------------------------------------------------------------------------------------------------------------------------
query = 2
object1 = Solution()
print(object1.grayCode(query))
#------------------------------------------------------------------------------------------------------------------------------------------------------------