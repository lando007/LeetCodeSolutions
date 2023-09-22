from typing import List
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 """
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #sorted values to 122
        #Sets the number to incriment by
        count = 0
        #Sorts the Array so the values will always be by each other when comparing
        sortednums = sorted(nums)
        #if there is only one value in the Array return the value
        if  len(sortednums == 1):
            return sortednums[0]
        #if the count is less the the length of the Array then continue looping
        while count <= len(nums)-1:
            #Checks the values of the array at space count and one location above that
            if sortednums[count] == sortednums[count+1]:
                #incriments the count by 2 to skip the one value compared above it
                count += 2
                #if the count + 1 is the length of the sorted array then that means the last value is the one without a pair
                if count + 1 == len(sortednums):
                    return sortednums[count]
            #if the two values dont equal each other then return the value at location count
            else:
                return(sortednums[count])


example = [1,1,2,3,3]
print(Solution().singleNumber(example))
