class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        
        stack = []
        operators = {'-', '+', '/', '*'}
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            
            else:
                second = stack.pop()
                first = stack.pop()

                if i == '+':
                    result = first + second
                elif i == '-':
                    result = first - second
                elif i == '/':
                    if second == 0:
                        result = 0
                    else:
                        result = first / second 
                        result = int(result)
                else:
                    result = first * second

                stack.append(result)
                
        
        return stack[0]
        