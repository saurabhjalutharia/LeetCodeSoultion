import os
os.system("cls")
#----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def removeElement(self, inputList, target):
        i = 0									#RETURN VALUE. DEFAULT 0
        for num in inputList:					#LOOP FOR ALL INTEGERS IN THE LIST
            if num != target:					#CHECK CURRENT LOOPED NUMBER EQUALS OR NOT EQUALS TO TARGET VALUE
                inputList[i] = num 				#IF NOT EQUAL REPLACE THE ith VALUE FROM THE INPUT LIST TO CURRENT NUMBER
                i += 1							#INCREMENT THE ith VALUE, MEANS THESE ARE THE TOTAL NUMBER THAT ARE NOT =! TO TARGET VALUE
        return i
#----------------------------------------------------------------------------------------------------------------------------------------------------
query = [3,2,1,3]
val = 3
object1 = Solution()
print(object1.removeElement(query, val))
#----------------------------------------------------------------------------------------------------------------------------------------------------

# query = [0,1,2,2,3,0,4,2]
# val = 2