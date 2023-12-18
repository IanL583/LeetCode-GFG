class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in maps:
                return [maps[diff], i]
            maps[v] = i