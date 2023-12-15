class Solution:
    def intToRoman(self, num: int) -> str:

        numRomanList = [
            ["I", 1], ["IV", 4], ["V", 5], ["IX", 9], 
            ["X", 10], ["XL", 40],["L", 50], ["XC", 90], 
            ["C", 100],["CD", 400], ["D", 500], ["CM", 900], 
            ["M", 1000]]

        check = "2" * 2
        print(check)         

        res = ""
        for sym, value in reversed(numRomanList):
            if num // value:
                c : int = num // value
        
                res += (sym * c)
                num = num % value   

        return res                 

print(Solution().intToRoman(2000))