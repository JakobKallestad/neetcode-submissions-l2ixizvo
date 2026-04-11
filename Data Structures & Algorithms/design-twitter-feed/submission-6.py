import heapq

class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.user_following = defaultdict(set)
        self.time = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_following[userId]:
            self.user_following[userId].add(userId)
        self.user_tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        #user = self.user_tweets[userId]
        feed_users = [] #user
        for fu in self.user_following[userId]:
            feed_users.append(self.user_tweets[fu])
        
        fu_ids = [-1]*len(feed_users)
        heap = []
        for uid, fu in enumerate(feed_users):
            if len(fu) > 0:
                t, twid = fu[-1]
                heap.append((t, twid, uid))
        heapq.heapify_max(heap)

        res = []
        for i in range(10):
            if not heap:
                break
            t, twid, uid = heapq.heappop_max(heap)
            res.append(twid)
            fu_ids[uid] -= 1
            if len(feed_users[uid]) >= abs(fu_ids[uid]):
                t2, twid2 = feed_users[uid][fu_ids[uid]]
                heapq.heappush_max(heap, ((t2, twid2, uid)))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId in self.user_following[followerId]:
            self.user_following[followerId].remove(followeeId)
        
