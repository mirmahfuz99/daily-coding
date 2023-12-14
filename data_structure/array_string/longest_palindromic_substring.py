class Solution:
    def longestPalindrome(self, s:str) -> str:

        res = ''

        # use nested loops to generate all possible substrings of the input string
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):

                tempString = s[i:j]
            
                if tempString == tempString[::-1]:
                    if len(tempString) > len(res):
                        res = tempString

        return res          



print(Solution().longestPalindrome("babad"))