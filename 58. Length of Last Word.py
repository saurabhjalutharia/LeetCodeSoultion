import os
os.system("cls")

class Solution(object):
    def lengthOfLastWord(self, s):
        length = 0                  #INITIAL LENGTH/DEFAULT = 0
        for i in reversed(s):       #REVERSE THE STRING(query)
            if i == ' ':            #GO BACK TILL WE FIND THE FIRST BLANK/WHITE SPACE
                if length:          #IF WE FOUND A SPACE AND LENGTH IS 0 BREAK THE LOOP
                    break
            else:
                length += 1         #ADD ONE IN LENGTH FOR EVERY WORD 
        return length
#-------------------------------------------  ALTERNATE METHOD  ----------------------------------------------------
class Solution2(object):
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])
#---------------------------------------------  CLASS OBJECT ------------------------------------------------------
query = "Hello World"
object1 = Solution()
print(object1.lengthOfLastWord(query))