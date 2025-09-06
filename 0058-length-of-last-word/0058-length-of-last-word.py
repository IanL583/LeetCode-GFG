class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.strip()
        if ' ' not in string:
            return len(string)
        new_string = string[::-1]
        count = 0
        for letter in new_string:
            if letter is not ' ':
                count += 1
            if letter is ' ':
                return count
