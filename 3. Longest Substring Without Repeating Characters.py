import os, collections
os.system("cls")
#----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def lengthOfLongestSubstring(self, inputString):
        result = 0
        stringLength = 0
        count = collections.Counter()

        for index, character in enumerate(inputString):
            count[character] += 1
            while count[character] > 1:
                count[inputString[stringLength]] -= 1
                stringLength += 1s
            result = max(result, index - stringLength + 1)
        return result
#----------------------------------------------------------------------------------------------------------------------------------------------------
query = "abcabcbb"
object1 = Solution()
print(object1.lengthOfLongestSubstring(query))
#----------------------------------------------------------------------------------------------------------------------------------------------------