class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr_total = sum(nums)
        actual_total = sum(range(0, len(nums) + 1))
        return actual_total - curr_total 
        