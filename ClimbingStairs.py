#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step"""

class Solution:
    def climbStairs(self, n: int) -> int:
        #set starting number to itterate through
        i = 2
        #set what the current value is
        currentValue = 1
        #set what the previous value was
        previousValue = 1
        #if the value is 0 or 1 return the value 1
        if n == 0 or n == 1:
            return 1
        else:
            #while the value is between 2 and n + 1 continute to count up the amounts of ways to step up
            while i < n + 1:
                #Set the temp value to the current value to save for the prevousvalue after adding it
                temp = currentValue
                #set the current value to the currentvalue + the prevousValue
                currentValue = previousValue + currentValue
                #set the old current value stored in temp to the previous value for the next itterantion
                previousValue = temp
                #incriment i
                i += 1
        #set the current value at the end to n and return that value back
        n = currentValue
        return n
value = 4
print(Solution().climbStairs(value))

