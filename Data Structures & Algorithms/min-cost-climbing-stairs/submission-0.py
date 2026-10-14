class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        M = [0] * (n + 1)
        for j in range(n, -1, -1):
            if j == n:
                M[j] = 0
            elif j == n - 1:
                M[j] = cost[n - 1]
            else:
                M[j] = cost[j] + min(M[j + 1], M[j + 2])
        
        return min(M[0], M[1])
        