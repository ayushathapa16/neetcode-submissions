class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        M = [[None] * (amount + 1) for _ in range(n + 1)]
        for i in range(0, n + 1):
            for j in range(0, amount + 1):
                if j == 0:
                    M[i][j] = 1
                elif i == 0 and j != 0:
                    M[i][j] = 0
                elif coins[i - 1] > j:
                    M[i][j] = M[i - 1][j]
                else:
                    M[i][j] = M[i - 1][j] + M[i][j - coins[i - 1]]
        return M[n][amount]
        
    
        