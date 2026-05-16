#
# @lc app=leetcode id=895 lang=python
#
# [895] Maximum Frequency Stack (HARD)
#
# PROBLEM:
# Implement a FreqStack with:
# - push(val): push val onto stack
# - pop(): remove and return the most frequent element (ties: most recently pushed)
#
# APPROACH: Three maps:
# - freq: val → its frequency
# - group: freq → stack of elements with that frequency
# - maxfreq: current maximum frequency

# @lc code=start
from collections import defaultdict

class FreqStack(object):

    def __init__(self):
        self.freq  = defaultdict(int)
        self.group = defaultdict(list)  # freq → list of vals (stack order)
        self.maxfreq = 0

    def push(self, val):
        self.freq[val] += 1
        f = self.freq[val]
        self.maxfreq = max(self.maxfreq, f)
        self.group[f].append(val)

    def pop(self):
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return val
        # Time: O(1) each  Space: O(n)
# @lc code=end
