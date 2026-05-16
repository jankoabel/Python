#
# @lc app=leetcode id=355 lang=python
#
# [355] Design Twitter
#
# PROBLEM:
# Design a simplified version of Twitter where users can:
#   - postTweet(userId, tweetId): Post a tweet.
#   - getNewsFeed(userId): Return 10 most recent tweet ids in the user's news feed
#     (their own tweets + tweets from users they follow), most recent first.
#   - follow(followerId, followeeId): Follower follows a followee.
#   - unfollow(followerId, followeeId): Follower unfollows a followee.
#
# APPROACH: Heap merge of each followed user's tweet list.
# Keep a global timestamp counter. Each user has a list of (timestamp, tweetId).
# For getNewsFeed: collect the latest tweet pointer from each followed user,
# use a max-heap (negate timestamp) to merge up to 10 tweets.

# @lc code=start
from collections import defaultdict
import heapq

class Twitter(object):

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)   # userId -> [(timestamp, tweetId)]
        self.following = defaultdict(set) # userId -> set of followeeIds

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        # Collect candidates: self + all followed users
        heap = []
        candidates = self.following[userId] | {userId}
        for uid in candidates:
            tweets = self.tweets[uid]
            if tweets:
                idx = len(tweets) - 1
                ts, tid = tweets[idx]
                # Max-heap via negative timestamp
                heapq.heappush(heap, (-ts, tid, uid, idx - 1))

        result = []
        while heap and len(result) < 10:
            neg_ts, tid, uid, idx = heapq.heappop(heap)
            result.append(tid)
            if idx >= 0:
                ts, next_tid = self.tweets[uid][idx]
                heapq.heappush(heap, (-ts, next_tid, uid, idx - 1))

        return result

    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)
        # Time: getNewsFeed O(k log k) where k = number of followees
        # Space: O(n) tweets + O(n) follows
# @lc code=end
