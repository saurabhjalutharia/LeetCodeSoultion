import os
os.system("cls")
#----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution():
    def minimumAbsDifference(self, inputList):
        resultList = []                                                 #FINAL RETURN LIST.DEFAULT EMPTY
        minimumValue = 999999                                           #SET MINIMUM VALUE AMONG THE LIST.DEFAULT INF i.e. 999999
        inputList.sort()                                                #SORT INPUT LIST IN ASSECENDING ORDER

        for i in range(len(inputList) - 1):                             #LOOP TILL LENGTH OF INPUT LIST
            difference = inputList[i + 1] - inputList[i]                #FIND DIFFERENCE BETWEEN CURRENT NUMBER TO ITS NEXT NUMBER
            if difference < minimumValue:
                minimumValue = difference                               #NEW DIFFERENCE IS LESS THAN CURRENT MINIMUM VALUE SET NEW MINIMUM VALUE
                resultList = []                                         #RESET RESULT LIST TO DEFAULT EMPTY LIST
            if difference == minimumValue:                              #IF NEW DIFFERENCE IS EQUALS TO ALREADY SET MINIMUM VALUE THEN
                resultList.append([inputList[i], inputList[i + 1]])     #ADD THE CURRENT LOOP i VALUE AND NEXT VALUE TO THE RESULT LIST
        return resultList                                               #RETURN THE FINAL RESULT LIST    
#----------------------------------------------------------------------------------------------------------------------------------------------------
query = [4,6,1,7,9]
object1 = Solution()
print(object1.minimumAbsDifference(query))
#----------------------------------------------------------------------------------------------------------------------------------------------------

    