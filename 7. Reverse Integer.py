import os
os.system("cls")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution():
    def reverse_integer(self, n):
        y = str(abs(n))                         #CONVERT THE INTERGER VALUE INTO ABSOLUTE VALUE FOR NEGATIVE NUMBER
        y = y.strip()                           #BY USING STRIP FUNCTION CONVERT THE STRING INT VALUE INTO LIST VALUE FOR SLICE OPERATION
        y = y[::-1]                             #REVERSE THE LIST
        output = int(y)                         #CONVERT THE LIST VALUES INTO INT VALUE
        if output >= 2** 31 -1 or output <= -2** 31:            #MAX AND MIN LIMIT
            return 0
        elif n < 0:                                             #IF INPUT VALUE WAS NEGATIVE VALUE ADD '-'
            return -1 * output
        else:
            return output
#------------------------------------------------------------------------------------------------------------------------------------------------------------
query = 123
object1 = Solution()
print(object1.reverse_integer(query))
#------------------------------------------------------------------------------------------------------------------------------------------------------------