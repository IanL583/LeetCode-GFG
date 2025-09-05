class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for num in nums:
            if num not in unique:
                unique.add(num)
            else:
                return True
        return False