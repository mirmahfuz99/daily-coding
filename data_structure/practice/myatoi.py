
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        result = 0  # Stores and returns the integer converted value for str
        i = 0  # just a current character pointer for string
        sign = 1  # multiplied at the end to result to determine if the string is +ve or -ve
        if i < len(s) and s[i] in ['-', '+']:  # Check the sign of string (+ or -)
            if s[i] == '-':
                sign = -1
            i += 1

        # Now traverse the entire string and convert it into integer
        while i < len(s) and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            result = result * 10 + digit
            i += 1

        value = result * sign
        #check for integer overflow or underflow
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)
        return value


print(Solution().myAtoi(" -123a"))





