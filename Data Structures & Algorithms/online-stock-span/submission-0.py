class StockSpanner:

    def __init__(self):

        self.curr = 0
        self.stack = [(math.inf, 0)] # (price, day)
        

    def next(self, price: int) -> int:
        
        self.curr += 1

        while self.stack[-1][0] <= price:
            self.stack.pop()

        self.stack.append((price, self.curr))

        return self.curr - self.stack[-2][1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)