import os
os.system("cls")
#--------------------------------------------------------------------------------------------------------------------------------------------------
class Solution(object):
    def generateParenthesis(self, n):
        resultList = []                                             #FINAL OUTPUT VALUES LIST. DEFAULT EMPTY
        self.generateParenthesisUtil(n, n, "", resultList)          #CALL FUNCTION WITH LEFT AND RIGHT PARENTHESES VALUES EQUAL TO AS USER INPUT
        return resultList                                           #AND TEMP VALUE AS NOTHING AND RESULT LIST AS EMPTY
    def generateParenthesisUtil(self, leftParentheses, rightParentheses, temp, resultList):
        if leftParentheses == 0 and rightParentheses == 0:          #WHEN BOTH LEFT AND RIGHT PARENTHESE EXHAUSTED ADD TO RESULT LIST
            resultList.append(temp)
            return
        if leftParentheses > 0:                                     #CALL FUNTION RECURSIVELY WITH ONE LEFT PARENTHESE LESS THAN PREVIOUS ONE
            self.generateParenthesisUtil(leftParentheses-1, rightParentheses, temp +'(', resultList)
        if rightParentheses > leftParentheses:                      #CALL FUNTION RECURSIVELY IF RIGHT PARENTHESE IS MORE THAN LEFT ONE
            self.generateParenthesisUtil(leftParentheses, rightParentheses-1, temp + ')', resultList)
#------------------------------------------------------------------------------------------------------------------------------------------------------
query = 4
object1 = Solution()
print(object1.generateParenthesis(query))