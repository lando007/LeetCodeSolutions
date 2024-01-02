"""Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"""

from typing import List
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        intnum1 = int(num1)
        intnum2 = int(num2)
        combinednum = intnum1 * intnum2
        strcombinednum = str(combinednum)
        return strcombinednum

num1, num2 = "123", "456"

test = Solution().multiply(num1, num2)
print(test)
