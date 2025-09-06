class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(filter(str.isalnum, s)).lower()
        end = len(clean_s) - 1
        for i in range(end):
            if clean_s[i] == clean_s[end]:
                end -= 1
            else:
                return False
        return True

