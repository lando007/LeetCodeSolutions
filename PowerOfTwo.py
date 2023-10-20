"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        powerOfTwo = 2
        x = 2
        if n == 1:
            return True
        elif n <= 0:
            return False
        while powerOfTwo < n:
            powerOfTwo = powerOfTwo * x
            if powerOfTwo > n:
                return False
            if powerOfTwo == n:
                return True
        return powerOfTwo
example = -16
print(Solution().isPowerOfTwo(example))
