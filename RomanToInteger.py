s = "II"
class Solution:

    def romanToInt(self, s: str) -> int:
        count = 0
        backcount = ""
        for c in s:
            if c == "I":
                count += 1
            if c == "V":
                count += 5
                if backcount == "I":
                    count -= 2
                    print(c)
            if c == "X":
                count += 10
                if backcount == "I":
                    count -= 2
                    print(c)
            if c == "L":
                count += 50
                if backcount == "X":
                    count -= 20
                if backcount == "V":
                    count -= 10
                if backcount == "I":
                    count -= 2
            if c == "C":
                count += 100
                if backcount == "X":
                    count -= 20
            if c == "D":
                count += 500
                if backcount == "C":
                    count -= 200
            if c == "M":
                count += 1000
                if backcount == "C":
                    count -= 200
                    backcount

            backcount = c
        return count
    a = "MMMCMXCIX"
    R = romanToInt(a, a)
    print(R)
