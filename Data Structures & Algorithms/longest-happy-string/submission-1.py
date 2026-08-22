class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        heap = []
        if a:
            heapq.heappush_max(heap, (a, ord('a')))
        if b:
            heapq.heappush_max(heap, (b, ord('b')))
        if c:
            heapq.heappush_max(heap, (c, ord('c')))

        res = ""

        while heap:
            freq, char = heapq.heappop_max(heap)

            char = chr(char)

            if len(res) > 1 and res[-1] == char and res[-2] == char:
                

                if heap:
                    freq2, char2 = heapq.heappop_max(heap)
                    char2 = chr(char2)
                    res += char2
                    if freq2 > 1:
                        heapq.heappush_max(heap, (freq2 - 1, ord(char2)))

                    heapq.heappush_max(heap, (freq, ord(char) ))

            else:
                res += char
                if freq > 1:
                    heapq.heappush_max(heap, (freq - 1, ord(char) ))

        return res


        
        