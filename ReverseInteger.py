"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""
class Solution:
    def reverse(self, x: int) -> int:
            value = str(x)
            value = value[::-1]
            if value[-1] == "-":
                value = value[:-1]
                value = "-"+ value
            if abs(int(value)) >= 2147483648:
                return 0
            return int(value)
example = 1534236469
print(Solution().reverse(example))
