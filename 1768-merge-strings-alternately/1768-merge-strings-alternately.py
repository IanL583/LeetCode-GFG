class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        newString = ""
        count = 0
        while (count < len(word1) or count < len(word2)):
            if count < len(word1):
                newString += word1[count] 
            if count < len(word2):
                newString += word2[count]
            # need to increment the loop if it is not a for loop
            count += 1
        return newString