class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {']':'[', '}':'{', ')': '('}

        stack = []
        for bracket in s:
            # if it is a closing bracket
            if bracket in pairs:
                if stack and stack[-1] == pairs[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return not stack