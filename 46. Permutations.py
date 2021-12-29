import os
os.system("cls")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def permute(self, inputList):
        resultList = []                                     #FINAL RETURN LIST OF VALUES
        visitedList = [False] * len(inputList)              #CHECK WHETHER EACH ITEM IN THE LIST VISITED ALONG WITH ITS DEPTH

        def depthSearch(path):                              #PATH REPRESENT THE DEPTH OF THAT CURRENT LIST ITEM
            if len(path) == len(inputList):                 #IF DEPTH IS EQUAL TO THE INPUT LENGTH MEANS TRAVERSE S COMPLETE
                resultList.append(path)                     #ADD THE DEPTH PATH TRAVESE LIST INTO THE RESULT LIST
                return
            for i in range(len(inputList)):                 #LOOP TILL INPUT LIST GET EXHAUSTED
                if visitedList[i]:                          #IF ITEM IS ALREADY VISITED DO NOTHING
                    continue
                visitedList[i] = True                       #SET CURRENTLY ITERATED ITEM VALUE TO TRUE, MEANS NOW WE GO IN DEPTH OF THAT ITEM VALUE
                depthSearch(path + [inputList[i]])          #RECURSIVELY CALL THE DEPTHSEARCH FUNTION WITH NEW PARAMETER
                visitedList[i] = False                      #SET CURRENTLY ITERATED ITEM VALUE TO FALSE, MEANS NOW WE BACKTRACK TO STARTING POINT
        depthSearch([])                                     #TO START THE FUNCTION.BY DEFAULT PASS AN EMPTY LIST
        return resultList
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
query = [1,2,3]
object1 = Solution()
print(object1.permute(query))
#------------------------------------------------------------------------------------------------------------------------------------------------------------