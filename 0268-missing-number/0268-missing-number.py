class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target_sum = 0
        for i in range(1, len(nums) + 1):
            target_sum += i
        return target_sum - sum(nums)