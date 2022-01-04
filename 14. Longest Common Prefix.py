import os
os.system("cls")
#----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution():
    def longestCommonPrefix(self, inputSringList):
        lcpString = ""                                                     #EMPTY STRING
        if inputSringList is None or len(inputSringList) == 0:             #BASE CONDITION
            return lcpString
        
        minimumLength = len(inputSringList[0])                             #CONSIDER THE FIRST STRING IS THE MINIMUM STRING LENGTH AMONG ALL THE STRINGS
        for i in range(1, len(inputSringList)):
            minimumLength = min(minimumLength, len(inputSringList[i]))     #FIND MINIMUM LENGTH STRING AMONG ALL STRINGS IN THE LIST
       
        for i in range(0, minimumLength):                                  #LOOP UNTILL STRING WITH MINIMUM LENGTH GET EXHAUTED
            currentCharacter = inputSringList[0][i]                        #GET THE CURRENT CHARACTER FROM THE FIRST STRING
            for j in range(0, len(inputSringList)):
                if inputSringList[j][i] != currentCharacter:               #CHECK IF CURRENT CHARACTER IS MATCH IN ALL OTHER STRINGS OR NOT
                    return lcpString
            lcpString += currentCharacter
        return lcpString
#----------------------------------------------------------------------------------------------------------------------------------------------------
query = ["flower","flow","flight"]
object1 = Solution()
print(object1.longestCommonPrefix(query))
#----------------------------------------------------------------------------------------------------------------------------------------------------