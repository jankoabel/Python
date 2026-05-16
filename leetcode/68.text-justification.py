#
# @lc app=leetcode id=68 lang=python
#
# [68] Text Justification (HARD)
#
# PROBLEM:
# Given words and a maxWidth, format the text such that each line has exactly
# maxWidth characters and is fully justified. Extra spaces distributed left-to-right.
# Last line is left-justified.
# Example: words=["This","is","an","example","of","text","justification."], maxWidth=16
#          → ["This    is    an","example  of text","justification.  "]
#
# APPROACH: Greedy line-packing. For each line, add words while they fit.
# Then distribute spaces: total_spaces / gaps (evenly), extra to leftmost gaps.

# @lc code=start
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lines = []
        i = 0
        while i < len(words):
            line_len = len(words[i])
            j = i + 1
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            lines.append(words[i:j])
            i = j

        result = []
        for k, line in enumerate(lines):
            if k == len(lines) - 1 or len(line) == 1:
                # Last line or single word: left-justify
                text = ' '.join(line)
                result.append(text + ' ' * (maxWidth - len(text)))
            else:
                total_spaces = maxWidth - sum(len(w) for w in line)
                gaps = len(line) - 1
                space, extra = divmod(total_spaces, gaps)
                text = ''
                for m, word in enumerate(line[:-1]):
                    text += word + ' ' * (space + (1 if m < extra else 0))
                text += line[-1]
                result.append(text)

        return result
        # Time: O(n * maxWidth)  Space: O(n)
# @lc code=end
