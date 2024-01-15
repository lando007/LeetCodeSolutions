"""Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.


Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits."""

from typing import List
class Solution:
    def hammingWeight(self, n: int) -> int:
        myDictionary = {}
        stringN = bin(n)[2:]
        print(stringN)
        for x in stringN:
            if x in myDictionary:
                myDictionary[x] += 1
            else:
                myDictionary[x] = 1
        if "1" in myDictionary:
            return myDictionary["1"]
        else: return 0



nums = 0b00000000000000000000000000000000

test = Solution().hammingWeight(nums)
print(test)
