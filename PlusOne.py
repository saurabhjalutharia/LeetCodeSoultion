import os
os.system("cls")

class Solution():
    def plusOne(self, digits):
      number = ""
      for i in digits:
         number += str(i)       #CONVERT EACH NUMBER FROM LIST TO STRING FORM
      number = int(number)      #CONVERT ALL STRING NUMBER INTO AN ONE INT NUMBER   
      number += 1               #ADD 1 IN THAT NUMBER
      number = str(number)      #CONVERT ALL THE NUMBER AGAIN TO STRING TYPE
      ansList = []
      for i in number:
         ansList.append(int(i))     #FOR EACH NUMBER CONVERT IT INTO INT AND ADD INTO LIST
      return ansList

digitsList = [5,3,2,4]
ob1 = Solution()
print(ob1.plusOne(digitsList))