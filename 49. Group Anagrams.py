import os, collections
os.system("cls")
#----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def groupAnagrams(self, inputStringList):
        dictionary = collections.defaultdict(list)
        for item in inputStringList:
            keyValue = ''.join(sorted(item))
            dictionary[keyValue].append(item)
        return dictionary.values()
#----------------------------------------------------------------------------------------------------------------------------------------------------
query = ["eat","tea","tan","ate","nat","bat"]
object1 = Solution()
print(object1.groupAnagrams(query))
#----------------------------------------------------------------------------------------------------------------------------------------------------