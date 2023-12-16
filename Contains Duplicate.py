"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true"""

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myDictionary = {}

        for x in nums:
            if x in myDictionary:
                myDictionary[x] +=1
            else:
                myDictionary[x] = 1

        for y in nums:
            if myDictionary[y] >= 2:
                return True
            else: continue
        return False

nums = [2,14,18,22,22]
test = Solution().containsDuplicate(nums)
print(test)

