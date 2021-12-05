import os,copy
os.system("cls")


class Solution:
    def maxPointerroduct(self, query):
        result = query[0]
        minPointer = query[0]
        maxPointer = query[0]
        for a in query[1:]:
            temp_maxPointer = maxPointer
            temp_minPointer = minPointer
            maxPointer = max(max(temp_maxPointer*a, temp_minPointer*a), a)
            minPointer = min(min(temp_maxPointer*a, temp_minPointer*a), a)
            result = max(result, maxPointer)
        return result         
        
que = [-1,-1,2]
obj = Solution
print(Solution.maxPointerroduct(obj, que))