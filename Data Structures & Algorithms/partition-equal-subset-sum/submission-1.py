class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # sum is odd and cannot be partitioned 
        if sum(nums) % 2 != 0:
            return False
        
        S = sum(nums) // 2
        n = len(nums)
        M = [[None] * (S + 1) for _ in range(n + 1)]

        for i in range(0, n + 1):
            for j in range(0, S + 1):
                if j == 0:
                    M[i][0] = True
                elif i == 0 and j != 0:
                    M[0][j] = False
                elif nums[i - 1] > j:
                    M[i][j] = M[i - 1][j]
                else:
                    M[i][j] = M[i - 1][j] or M[i - 1][j - nums[i - 1]]
        
        return M[n][S]

        