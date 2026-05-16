#
# @lc app=leetcode id=1268 lang=python
#
# [1268] Search Suggestions System
#
# PROBLEM:
# Given a list of products and a search word, for each prefix of searchWord
# return the 3 lexicographically smallest products that have that prefix.
# Example: products=["mobile","mouse","moneypot","monitor","mousepad"],
#          searchWord="mouse"
#          → [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],
#             ["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
#
# APPROACH: Sort products. Use binary search to find the starting position
# of each prefix, then take up to 3 products from there.

# @lc code=start
import bisect

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        result = []
        prefix = ""

        for c in searchWord:
            prefix += c
            # Find leftmost position where prefix fits
            pos = bisect.bisect_left(products, prefix)
            suggestions = []
            for i in range(pos, min(pos + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break
            result.append(suggestions)

        return result
        # Time: O(n log n + m log n)  Space: O(n)
# @lc code=end
