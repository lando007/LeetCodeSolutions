"""Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself."""
from typing import List
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #Make an empty array to put the end result of the combination of the two strings
        arrayValues = []
        #Tracks the value of the combined values
        carryOver  = 0
        #sets the length of how often the loops should be run based ons string a
        x = len(a) - 1
        #sets the length of how often the loops should be run based ons string b
        y = len(b) - 1
        #Loops throught the length of each value or if a value is still in CarryOver
        while x >= 0 or y >= 0 or carryOver:
            #if the length of x is not less there zero there is a value that needs to be added to caryOver
            if x>= 0:
                #turns the character into an int and adds it to carryOver
                carryOver+= int(a[x])
                #subtracks one from x
                x -= 1
            if y >= 0:
                #turns the character into an int and add it to the carryOver
                carryOver += int(b[y])
                #subtracks one from y
                y -= 1
            # appends the value of caryover mod 2 to the arrayValues array
            arrayValues.append(str(carryOver % 2))
            #devids the value of cary over by 2 to make to cary over 1 or zero as it discards the remander
            carryOver //= 2
        
        return ''.join(reversed(arrayValues))
#string1 = "1010"
#string2 = "1011"
string1 = "1111"
string2 = "1111"
test = Solution().addBinary(string1,string2)
print(test)
