class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mcount = {}
        for letter in magazine:
            if letter in mcount:
                mcount[letter] += 1
            else:
                mcount[letter] = 1
        for letter in ransomNote:
            if letter not in mcount or mcount[letter] == 0:
                return False
            mcount[letter] -= 1
        return True