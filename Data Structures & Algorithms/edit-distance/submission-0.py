class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        M = [[None] * (m + 1) for _ in range(n + 1)]
        for i in range(0, n + 1):
            for j in range(0, m + 1):
                if i == 0:
                    M[i][j] = j
                elif j == 0:
                    M[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    M[i][j] = M[i - 1][j - 1]
                else:
                    M[i][j] = 1 + min(M[i - 1][j], M[i][j - 1], M[i - 1][j - 1])
        return M[n][m]
        