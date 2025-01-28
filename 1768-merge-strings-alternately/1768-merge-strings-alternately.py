class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        smaller_string = min(len(word1), len(word2))
        for letter in range(smaller_string):
            result += word1[letter] + word2[letter]
        result += word1[smaller_string:] + word2[smaller_string:]
        return result