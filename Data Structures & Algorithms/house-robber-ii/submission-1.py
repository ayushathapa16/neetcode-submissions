class Solution:
    def helper(self, nums: List[int]) -> int:
        n = len(nums)
        M = [0] * (n + 1)
        for j in range(1, n + 1):
            if j == 1:
                M[j] = nums[0]
            else:
                M[j] = max(M[j - 1], M[j - 2] + nums[j - 1])
        return M[n]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        else:
            return max(self.helper(nums[0:n - 1]), self.helper(nums[1:n]))

    

        
        