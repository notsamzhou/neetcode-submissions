class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        children = [(i, rating) for i, rating in enumerate(ratings)]

        
        children.sort(key = lambda x: x[1])

        candy = [0] * len(ratings)

        res = 0
        for i in range(len(ratings)):
            candy[children[i][0]] = 1
            idx = children[i][0]

            if idx > 0:
                neighbor = idx - 1
                if ratings[neighbor] < ratings[idx]:
                    candy[children[i][0]] = max(candy[children[i][0]], 1 + candy[neighbor])
            if idx < len(ratings)-1:
                neighbor = idx + 1
                if ratings[neighbor] < ratings[idx]:
                    candy[children[i][0]] = max(candy[children[i][0]], 1 + candy[neighbor])

            res += candy[children[i][0]]

        return res

        
            