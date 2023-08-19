from typing import List

class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Set the base Value to compare everything else to
        base = strs[0]
        # Set the length of the base value
        baseLength = len(base)

        #if the base value is 0 there means nothing is in the list and should be returned right away
        if baseLength == 0:
            return "No Values"
        # Iterate through he baseLengths values
        for i in range(baseLength):

            #loops through values in the list excluding the first base value
            for listValues in strs[1:]:
                print(strs[1:])
                #ensures that index value is not out of bounds for the word we are on
                #or the base value equals the list value
                if (i == len(listValues) or listValues[i] != base[i]):

                    return base[0:i]
        #returns if the base word is the shortest value
        return base


    a = ["flower", "flow", "flight"]

    test = longestCommonPrefix(a, a)
    print(test)

