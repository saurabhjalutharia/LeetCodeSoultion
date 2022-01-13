import os
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def firstPalindrome(self, words):
        for word in words:
            if word == word[::-1]:
                return word
        return ""

query =  ["abc","car","ada","racecar","cool"]
object1 = Solution()
print(object1.firstPalindrome(query))
#----------------------------------------------------------------------------------------------------------------------------------------------------