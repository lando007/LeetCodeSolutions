from typing import List
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits[0] == "1" or digits[0] == "0":
            return False
        else:
            x = 0
            two = "abc"
            three = "def"
            four = "ghi"
            five = "jkl"
            six = "mno"
            seven = "pqrs"
            eight = "tuv"
            nine = "wxyz"
            list = []

            for y in digits:
                if y == "2":
                    for x in two:
                        list.append(x)
            return list


example = "22"
print(Solution().letterCombinations(example))
