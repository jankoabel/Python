#
# @lc app=leetcode id=380 lang=python
#
# [380] Insert Delete GetRandom O(1)
#
# PROBLEM:
# Implement a data structure that supports insert, remove, and getRandom
# all in O(1) average time. getRandom must return each element with equal probability.
#
# APPROACH: Hash map + dynamic array.
# - val_to_idx maps value → index in the array
# - To remove: swap target with last element, update the swapped element's index, pop last

# @lc code=start
import random

class RandomizedSet(object):

    def __init__(self):
        self.vals = []
        self.val_to_idx = {}

    def insert(self, val):
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val):
        if val not in self.val_to_idx:
            return False
        idx = self.val_to_idx[val]
        last = self.vals[-1]
        # Move last element to the removed slot
        self.vals[idx] = last
        self.val_to_idx[last] = idx
        self.vals.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self):
        return random.choice(self.vals)
        # Time: O(1) each  Space: O(n)
# @lc code=end
