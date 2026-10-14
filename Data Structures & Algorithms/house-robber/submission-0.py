class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        M = [0] * (n + 1)
        for j in range(1, n + 1):
            if j == 1:
                M[j] = nums[0]
            else:
                M[j] = max(M[j - 1], nums[j - 1] + M[j - 2])
        return M[n]

        