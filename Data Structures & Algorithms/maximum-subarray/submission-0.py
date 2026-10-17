class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        first_entry = nums[0]
        global_max = first_entry
        curr_max = first_entry
        for i in range(1, len(nums)):
            curr_max = max(curr_max + nums[i], nums[i])
            global_max = max(curr_max, global_max)
        return global_max
        