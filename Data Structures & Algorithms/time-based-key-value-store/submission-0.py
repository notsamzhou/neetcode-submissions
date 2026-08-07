import bisect
class TimeMap:

    def __init__(self):
        self.lookup = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.lookup:
            self.lookup[key] = []

        idx = bisect.bisect_left(self.lookup[key], timestamp, key = lambda x: x[1])
        self.lookup[key].insert(idx, [value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.lookup:
            return ""

        idx = bisect.bisect_left(self.lookup[key], timestamp, key = lambda x: x[1])

        if idx >= 0:
            if idx < len(self.lookup[key]) and timestamp == self.lookup[key][idx][1]:
                return self.lookup[key][idx][0]
            
            if idx > 0:
                return self.lookup[key][idx-1][0]

        return ""
        
