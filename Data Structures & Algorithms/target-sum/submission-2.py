class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        T = sum(nums)

        if (T + target) % 2 != 0:
            return 0
        
        if abs(target) > T:
            return 0

        S = (T + target) // 2
        n = len(nums)

        M = [[None] * (S + 1) for _ in range(n + 1)]
        for i in range(0, n + 1):
            for j in range(0, S + 1):
                if j == 0 and i == 0:
                    M[i][0] = 1
                elif i == 0:
                    M[0][j] = 0
                elif nums[i - 1] > j:
                    M[i][j] = M[i - 1][j]
                else:
                    M[i][j] = M[i - 1][j] + M[i - 1][j - nums[i - 1]]
        return M[n][S]
        