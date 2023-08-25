from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = 1
        y = 2

        if digits[0] == 9 and len(digits) == 1:
            digits[0] = 1
            digits.append(0)
        elif digits[len(digits) - 1] == 9:
            digits[len(digits) - 1 ] += 1
            while digits[len(digits) - x] == 10:
                digits[len(digits) - y] += 1
                digits[len(digits) - x] = 0
                if digits[0] == 10:
                    digits[0] = 1
                    digits.append(0)
                x += 1
                y += 1


        elif digits[len(digits) - 1] < 9:
            digits[len(digits) - 1] += 1
        return digits

    test = [4,5,9,9,9]
    test = plusOne(test, test)
    print(test)
