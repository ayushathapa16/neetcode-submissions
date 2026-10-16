class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        curr_max = nums[0]
        curr_min = nums[0]
        global_max = nums[0]
        for i in range(1, n):
            temp = curr_max * nums[i]
            curr_max = max(nums[i], temp, curr_min * nums[i])
            curr_min = min(nums[i], temp, curr_min * nums[i])
            global_max = max(curr_max, global_max)
        return global_max


        