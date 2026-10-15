class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_M = [-math.inf] * (n + 1)
        min_M = [math.inf] * (n + 1)
        for j in range(1, n + 1):
            if j == 1:
                max_M[1] = nums[0]
                min_M[1] = nums[0]
            else:
                max_M[j] = max(nums[j - 1], max_M[j - 1] * nums[j - 1], min_M[j - 1] * nums[j - 1])
                min_M[j] = min(nums[j - 1], max_M[j - 1] * nums[j - 1], min_M[j - 1] * nums[j - 1])
        return max(max_M)

        