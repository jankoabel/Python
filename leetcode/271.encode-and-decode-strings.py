#
# @lc app=leetcode id=271 lang=python
#
# [271] Encode and Decode Strings
#

# @lc code=start
class Codec:
    def encode(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Encode each string as: len(s) + '#' + s
        # The '#' delimiter after the length lets us read exactly len(s) chars,
        # so we don't confuse '#' appearing inside strings with delimiters
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':   # find the '#' that ends the length prefix
                j += 1
            length = int(s[i:j])         # number of chars in this string
            result.append(s[j+1:j+1+length])   # read exactly 'length' chars
            i = j + 1 + length           # advance past this string
        return result
        # Time: O(n) encode and decode   Space: O(n)
# @lc code=end
