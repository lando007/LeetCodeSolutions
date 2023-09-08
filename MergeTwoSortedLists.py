
"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list."""
from typing import List, Optional
import collections
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Creates a new ListNode
        head = ListNode()
        #Sets the head to the current posistion
        current = head
        #While both lists currently have values in the list loop through each and compare them
        while list1 and list2:
            # If list1 is less than list2
            if list1.val < list2.val:
                #Set the current.next value to list1 value
                current.next = list1
                #Set list1.next to list1 value
                list1 = list1.next
            # if list1 is not less then list2 or if the values are the same then this block will run
            else:
                #Sets the list2 to curretn.next
                current.next = list2
                #Sets list2 to continue the next value
                list2 = list2.next
            #sets current pointer the selected next value
            current = current.next
        # Sets whatever remaining value is if one list is longer then the next to the current list
        if list1 != None:
            current.next = list1
        else:
            current.next = list2
        # returns the head.next value
        return head.next



test = ListNode()
test2 = ListNode()
test2.val = 2
solution = Solution().mergeTwoLists(test, test2)
print(solution)
