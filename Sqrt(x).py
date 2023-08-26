import math
class Solution:
    def mySqrt(self, x: int) -> int:
        sqrtValue = math.sqrt(x)
        newValue = math.floor(sqrtValue)
        return newValue
value = 8
print(Solution().mySqrt(value))

