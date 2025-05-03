class Solution:
    def myAtoi(self, s: str) -> int:
        is_positive, num = True, 0
        s_it = iter(s)
        for char in s_it:
            # 1. Whitespace
            if char == ' ':
                continue
            # 2. Signedness
            elif char == '-':
                is_positive = False
            elif char == '+':
                is_positive = True
            # 3. Conversion
            elif char in '0123456789':
                num = int(char)
            break

        # 3.Conversion
        max_int, min_int = 2**31 - 1, 2**31
        for char in s_it:
            if char in '0123456789':
                num = num * 10 + int(char)
                # 4. Rounding
                if is_positive and num > max_int:
                    return max_int
                elif not is_positive and num > min_int:
                    return -min_int
            else:
                break
        return num if is_positive else -num


if __name__ == "__main__":
    print(Solution().myAtoi(".1"))