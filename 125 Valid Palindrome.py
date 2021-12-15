import os
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def isPalindrome(self, inputString):
        result = ''
        for i in inputString:
            if i.isalnum():
                result += i.lower()
        
        if result == result[::-1]:
            return True
        return False

query =  "bob"
object1 = Solution()
print(object1.isPalindrome(query))
#----------------------------------------------------------------------------------------------------------------------------------------------------
