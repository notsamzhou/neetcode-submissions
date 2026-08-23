class FreqStack:

    def __init__(self):
        self.stacks = [[]]
        self.freq = {}
        

    def push(self, val: int) -> None:


        if val not in self.freq:
            self.freq[val] = 0

        self.freq[val] += 1

        if self.freq[val] >= len(self.stacks):
            self.stacks.append([val])

        else:
            self.stacks[self.freq[val]].append(val)
        

    def pop(self) -> int:
        res = self.stacks[-1].pop()
        self.freq[res] -= 1
        if len(self.stacks) > 1 and self.stacks[-1] == []:
            self.stacks.pop()

        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()