class MinStack:
    items: list
    min_items: list

    def __init__(self):
        self.items = []
        self.min_items = []
        
    def push(self, val: int) -> None:
        if not self.items:
            self.min_items.append(val)
        elif val < self.min_items[-1]:
            self.min_items.append(val)
        else:
            self.min_items.append(self.min_items[-1])
        
        self.items.append(val)
          

    def pop(self) -> None:
        if self.items:
            last_element = self.items.pop()
            last_min = self.min_items.pop()

    def top(self) -> int:
        if self.items:
            return self.items[-1]

    def getMin(self) -> int:
        if self.items:
            return self.min_items[-1]
        
