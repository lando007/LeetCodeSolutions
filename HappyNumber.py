"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.


 """
class Solution:
    def isHappy(self, n: int) -> bool:
        #Sets the int to a string to itterate through
        stringN = str(n)
        #value to hold the number of times the while statement has been run to make sure its not just looping
        value = 0
        #Checks to see if the string is a 1 which wuold indicate a perfect number
        while stringN != "1":
            combinedNumbers = 0
            #multiplies each number by itself and combines it
            for x in stringN:
                num = int(x)
                newNum = num*num
                combinedNumbers += newNum
            print(stringN)
            #converts the combined number back into a string to check and see if it is a perfect number
            stringN = str(combinedNumbers)
            value += 1
            #checks if the while statment has run 100 time or not
            if value == 100:
                return False
        return True
example = 19
print(Solution().isHappy(example))
