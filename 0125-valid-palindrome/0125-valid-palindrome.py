class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer approach 
        clean_s = ''.join(filter(str.isalnum, s)).lower()
        left, right = 0, len(clean_s) - 1
        while left < right:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
        return True
