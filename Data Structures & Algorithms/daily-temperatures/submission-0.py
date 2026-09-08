class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n == 1:
            return [0]

        result = [0] * n
        stack = []

        for i in range(0, n):
            if not stack:
                stack.append((temperatures[i], i))
            else:
                while stack and temperatures[i] > stack[-1][0]:
                    _, index = stack.pop()
                    index_diff = i - index
                    result[index] = index_diff
                stack.append((temperatures[i], i))
        
        return result

            

        