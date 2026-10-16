class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        first_entry = nums[0]
        if n == 1:
            return first_entry

        curr_max = first_entry
        curr_min = first_entry
        global_max = first_entry
        for i in range(1, n):
            temp = curr_max * nums[i]
            curr_max = max(nums[i], temp, curr_min * nums[i])
            curr_min = min(nums[i], temp, curr_min * nums[i])
            global_max = max(curr_max, global_max)
        return global_max


        