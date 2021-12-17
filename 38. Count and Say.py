import os
os.system("cls")
#----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def countAndSay(self, inputNumber):
        result = '1'                                                #FINAL RESULT VALUE.DEFAULT IS 1 IN CASE FOR ONLY ONE VALUE
        for i in range(1, inputNumber):                             #LOOP TILL USER INPUT
            count = 0                                               #COUNT TOTAL NUMBER OF DIGITS
            previousNum = '.'                                       #MAKE TWO POINTER PREVIOUS THAT POINTS TO THE PREVIOUS ONE VALUE
            currentString = ""                                      #AND CURRENT POINTER THAT POINTS TO THE CURRENT NUM VALUE OF THE STRING
            for num in result:                                      #LOOP TILL RESTULT STRING GET EXHAUSTED
                if num == previousNum or previousNum == '.':        #"." REPRESENT THE FIRST DIGIT OF THE SRING
                    count += 1                                      #COUNTER INCREMENT BY 1
                else:
                    currentString += str(count) + previousNum       #ADD COUNT VALUE AND PREVIOUS NUM VALUE INTO THE CURRENT STRING 
                    count = 1                                       #RESET COUNTER TO ONE
                previousNum = num                                   #PREVIOUS VALUE BECOME CURRENT NUM VALUE IN LOOP OF RESULT STRING
            currentString += str(count) + previousNum
            result = currentString                                  #RESULT STRING BECOME CURRENT STRING VALUE
        return result
#----------------------------------------------------------------------------------------------------------------------------------------------------        
query = 4
object1 = Solution()
print(object1.countAndSay(query))
#----------------------------------------------------------------------------------------------------------------------------------------------------