# This is a sample Python script.
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def isPalidrome(self, x: int) -> bool:
        # for loop to check each location in the array
        # split integers
        # if else check if each integer is the same value as the last one and inciment down with each
        list_of_digits = list(map(int, str(x)))
        if x < 0:
            return False
        y = 0
        beggining_number = 0
        end_number = len(list_of_digits) - 1
        while y < len(list_of_digits):

            if list_of_digits[beggining_number] != list_of_digits[end_number]:
                print("your number is not a palidrome")
                return False
            elif list_of_digits[beggining_number] == list_of_digits[end_number]:

                print(beggining_number)
                print(end_number)
                if beggining_number == end_number or beggining_number == len(list_of_digits) - 1:
                    return True
                beggining_number += 1
                end_number -= 1
            elif beggining_number == end_number:
                print("this is what is happening")
                return True
            y += 1


p1 = Solution.isPalidrome(1, 11)
print(p1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
