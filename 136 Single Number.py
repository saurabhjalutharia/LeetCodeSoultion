import os
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------
class Solution():
    def singleNumber1(self, nums):
        numCountDict = {}                                   #DICTIONARY TO COUNT NUMBER OF OCCURRENCE OF EACH DIGIT
        for i in nums:
            numCountDict[i] = numCountDict.get(i, 0) + 1    #KEY = LIST NUMBER AND VALUE IS NUMBER OF TIMES ITS OCCURRED
                                                            #DEFAULT IS '0' ELSE 1 ADD EACH TIME IF SAME NUMBER OCCURRED MULTIPLE TIMES
        for key, value in numCountDict.items():             #LOOP DICTIONARY
            if value == 1:                                  #RETURN KEY THAT HAS VALUE 1 MEANS THAT OCCURRED ONLY ONCES IN THE LIST
                return key
#----------------------------------------------------------------------------------------------------------------------------------------------------
query = [4,1,4]
object1 = Solution()
print(object1.singleNumber1(query))
#----------------------------------------------------------------------------------------------------------------------------------------------------