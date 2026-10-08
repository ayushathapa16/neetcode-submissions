class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        M = [[None] * (m + 1) for _ in range(n + 1)]
        
        for i in range(0, n + 1):
            for j in range(0, m + 1):
                if i == 0 or j == 0:
                    M[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    M[i][j] = 1 + M[i - 1][j - 1]
                else:
                    M[i][j] = max(M[i - 1][j], M[i][j - 1])

        return M[n][m]
        