class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # intialise 2 pointers
        left, right = 0, len(nums) - 1
        # loop through the array and split array accordingly
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        # if nothing found
        return -1