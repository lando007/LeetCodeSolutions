class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        lastWord = words[len(words) -1]
        return len(lastWord)
    test = "Hello World"
    test = lengthOfLastWord(test, test)
    print(test)
