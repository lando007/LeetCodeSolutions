"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k."""
"""Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted."""
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Sets the current value to iterate the loop through. Starts at 1 because need to compare to last value 0
        i = 1
        #value to set the next unique value to
        j = 1
        #Loops through the length of the list
        while i < len(nums):
            #If the last value is the same as the current value then run
            if nums[i] != nums[i-1]:
                #set the current value to the next value in the list
                nums[j] = nums[i]
                #Iterate the next value to place int in the list
                j+=1
            #Iterate the next value in the list
            i+=1
        #delete all remaining value after removeing and moving forward all the unique values
        del nums[j:len(nums)]
        print(j)
        return nums
value = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(value))
