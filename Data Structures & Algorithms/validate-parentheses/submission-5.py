class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {']':'[', '}':'{', ')': '('}
        stack = []
        i = 0
        while i < len(s):
            curr = s[i]
            if curr in pairs:
                if not stack or stack[-1] != pairs[curr]:
                    return False
                stack.pop()
            else:
                stack.append(curr)
            i += 1
        return len(stack) == 0
        