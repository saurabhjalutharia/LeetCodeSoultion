import os
os.system("cls")

NumToAlphaDict = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",             #DICTIONARY NUMBER AS KEY AND ASSOCIATED ALPHABET AS KEY-VALUE
                   '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def letterCombinations(self, DigitInput):
        digitInputLength = len(DigitInput)                  #TOTAL LENGTH OF THE INPUT
        ans = []                                            #AN EMPTY LIST
        if DigitInput == "":
            return []                                       #IF USER ENTER NOTHING RETURN AN EMPTY LIST
        def bfs(position, string):                          #FIRST LETTER OF THE USER INPUT AS POSITION AND KEY-VALUE OF POSIION AS STRING
            if position == digitInputLength:                #WHEN POSITION VALUE BECOME EQUALS TO INPUT ADD GENERATED STRING INTO THE ANS LIST
                ans.append(string)
            else:
                letters = NumToAlphaDict[DigitInput[position]]          #IT CONTAIN THE KEY-VALUE OF THE POSITION VALUE AS KEY TO 'NumToAlphaDict'
                for letter in letters:                                  #LOOP FOR EVERY KEY-VALUE CHARACTER RECURSIVELY
                    bfs(position+1, string+letter)
        bfs(0,"")                                                       #FOR DEFAULT POSITION VALUE IS '0'
        return ans
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
query = "23"
object1 = Solution()
print(object1.letterCombinations(query))