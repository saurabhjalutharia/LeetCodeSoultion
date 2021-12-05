import os
os.system("cls")

class Solution:
    def strStr(self, haystack, needle):
        if haystack is None or needle is None:          #BASE CONDITION
            return -1
        if haystack == needle:                          #SPECIAL CASE
            return 0

        needleLength = len(needle)                          #SEARCH STRING LENGTH(NEEDLE)
        for i in range(len(haystack) - needleLength + 1):   #LOOP AND SLIDING HAYSTACK WINDOW
            if haystack[i:i + needleLength] == needle:      #START FROM HAYSTACK FIRST CHARACTER AND ADD NEEDLE LENGTH
                return i                                    #AND MATCH IT AGAINST THE NEEDLE STRING
        return -1

haystack  = "Hello"
needle = "ll"
obj = Solution
print(Solution.strStr(obj, haystack, needle))        