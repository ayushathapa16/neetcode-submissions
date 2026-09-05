class MinStack:
    items: list

    def __init__(self):
        self.items = [] 
        
    def push(self, val: int) -> None:
        self.items.append(val)   

    def pop(self) -> None:
        last_element = self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return min(self.items)
        
