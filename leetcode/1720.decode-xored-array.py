#
# @lc app=leetcode id=1720 lang=python
#
# [1720] Decode XORed Array
#
# PROBLEM:
# There is a hidden integer array arr. You know encoded[i] = arr[i] XOR arr[i+1]
# and the first element arr[0] = first.
# Return the original array arr.
# Example: encoded=[1,2,3], first=1 → [1,0,2,1]
#
# APPROACH: Since encoded[i] = arr[i] XOR arr[i+1],
# we get arr[i+1] = arr[i] XOR encoded[i] (XOR is its own inverse).

# @lc code=start
class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        arr = [first]
        for e in encoded:
            arr.append(arr[-1] ^ e)
        return arr
        # Time: O(n)  Space: O(n)
# @lc code=end
