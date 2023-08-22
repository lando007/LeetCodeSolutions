

class Solution:
    def isValid(self, s: str) -> bool:

        # create value dictionary to check against
        dictionary = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        # create a stack to push and pop from
        stack = []
        # each character in s string is run through
        for character in s:
            # if each character is key of the dictionary and add it into the top of the stack
            if character in dictionary:
                # add characterinto the top of the stack
                stack.append(character)
            # Checks to see if the length of the stack is empty or if the character in the dictionary doesnt match the value of the key
            elif len(stack) == 0 or character != dictionary[stack.pop()]:
                return False
        # Everything passed successfully so return true
        return len(stack) == 0

    test = "()()()()"
    Solution = isValid(test, test)
    print(Solution)
