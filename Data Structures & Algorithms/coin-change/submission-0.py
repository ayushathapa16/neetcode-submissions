class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        M = [[None] * (amount + 1) for _ in range(n + 1)]
        for i in range(0, n + 1):
            for j in range(0, amount + 1):
                if j == 0:
                    M[i][0] = 0
                elif i == 0 and j != 0:
                    M[0][j] = float('inf')
                elif coins[i - 1] > j:
                    M[i][j] = M[i - 1][j]
                else:
                    M[i][j] = min(M[i - 1][j], 1 + M[i][j - coins[i - 1]])
        return -1 if M[n][amount] == float('inf') else M[n][amount]

        