class Solution:
    def climbStairs(self, n: int) -> int:
        M = [0] * (n + 1)
        for j in range(n, -1, -1):
            if j == n or j == n - 1:
                M[j] = 1
            else:
                M[j] = M[j + 1] + M[j + 2]
        return M[0]