class Twitter:

    def __init__(self):
        self.following = dict()
        self.tweets = dict()
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        if not userId in self.tweets:
            self.tweets[userId] = deque()

        if not userId in self.following:
            self.following[userId] = set([userId])
            
        
        self.tweets[userId].append((self.time, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()

        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        heap = []
        for following in (self.following[userId] | {userId}):
            for tweet in self.tweets[following]:
                heapq.heappush(heap, tweet)

                if len(heap) > 10:
                    heapq.heappop(heap)
        feed  = []
        while heap:
            feed.append(heapq.heappop(heap)[1])
        return feed[::-1]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set([followerId])

        if not followerId in self.tweets:
            self.tweets[followerId] = deque()

        if not followeeId in self.tweets:
            self.tweets[followeeId] = deque()

        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set([followerId])

        if not followerId in self.tweets:
            self.tweets[followerId] = deque()

        if not followeeId in self.tweets:
            self.tweets[followeeId] = deque()

        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

        
