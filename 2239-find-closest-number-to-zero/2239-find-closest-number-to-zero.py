class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = float('inf')
        for number in nums:
            if abs(number) < abs(largest) or (abs(number) == abs(largest) and number > largest):
                largest = number
        return largest
             