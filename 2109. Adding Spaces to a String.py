import os
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def addSpaces(self, s, spaces):
        res = ""
        spaces = set(spaces)
        for i,c in enumerate(s):
            if i in spaces:
                res += " "
            res += c
        return res

query =  s = "LeetcodeHelpsMeLearn" 
spaces = [8,13,15]
object1 = Solution()
print(object1.addSpaces(query, spaces))
#----------------------------------------------------------------------------------------------------------------------------------------------------