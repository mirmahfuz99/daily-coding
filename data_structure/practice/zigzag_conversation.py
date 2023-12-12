class ZigzagConversation:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if (r > 0 and r < numRows - 1 and 
                    i + increment - 2 * r < len(s)):
                    print(r)
                    print(i + increment -2 * r)
                    res += s[i + increment -2 * r]



        return res;            

print(ZigzagConversation().convert(s="PAYPALISHIRING", numRows=4))        