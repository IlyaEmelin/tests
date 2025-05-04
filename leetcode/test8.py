class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. Whitespace
        s = s.strip()

        # 2. Signedness
        is_positive, offset = True, 0
        if s:
            if s[0] == '+':
                offset += 1
            elif s[0] == '-':
                offset += 1
                is_positive = False

        # 3. Conversion
        start_num, end_num = -1, -1
        for i in range(offset, len(s)):
            if s[i] in '0123456789':
                start_num, end_num = i, i+1
            else:
                return 0
            offset += 1
            break

        # 3.Conversion
        for i in range(offset, len(s)):
            if s[i] in '0123456789':
                end_num = i+1
            else:
                break

        # 4. Rounding
        if start_num >=0:
            value = int(s[start_num:end_num])
            if is_positive:
                if (max_int := 2**31 - 1) < value:
                    return max_int
                return value
            else:
                if (min_int := 2**31) < value:
                    return -min_int
                return -value
        return 0


if __name__ == "__main__":
    print(".1", Solution().myAtoi(".1"), 0, sep='|')
    print("42", Solution().myAtoi("42"), 42, sep='|')
    print("   -042", Solution().myAtoi("   -042"), -42, sep='|')
    print("0 - 1", Solution().myAtoi("0 - 1"), 0, sep='|')
    print("1337c0d3", Solution().myAtoi("1337c0d3"), 1337, sep='|')
    print("0-1", Solution().myAtoi("0-1"), 0, sep='|')
    print("words and 987", Solution().myAtoi("words and 987"), 0, sep='|')
    print("-91283472332", Solution().myAtoi("-91283472332"), -2147483648, sep='|')
    print("", Solution().myAtoi(""), 0, sep='|')
    print(" ", Solution().myAtoi(" "), 0, sep='|')