import os
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def getDescentPeriods(self, prices):
        pos = [0]
        prev = -100
        for i,p in enumerate(prices):
            if prev == p + 1:
                pos.append(1)
            else:
                pos.append(0)
            prev = p
        
        print(pos)
        
        pos.append(0)
        
        res = 0
        cur = 0
        for x in pos:
            if x == 1:
                cur += 1
            else:
                res += (cur * (cur + 1)) // 2
                cur = 0
        return res + len(prices)


query =  [3,2,1,4]
object1 = Solution()
print(object1.getDescentPeriods(query))
#----------------------------------------------------------------------------------------------------------------------------------------------------