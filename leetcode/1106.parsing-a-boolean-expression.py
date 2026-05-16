#
# @lc app=leetcode id=1106 lang=python
#
# [1106] Parsing A Boolean Expression (HARD)
#
# PROBLEM:
# Evaluate a boolean expression:
#   't' = True, 'f' = False
#   '!(expr)' = NOT, '&(e1,e2,...)' = AND, '|(e1,e2,...)' = OR
# Example: "|(f,t)" → True  ;  "!(&(f,t))" → True
#
# APPROACH: Recursive descent parser or stack-based.
# Stack: push chars. On ')': collect operands, apply operator from context.

# @lc code=start
class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        def parse(s, idx):
            c = s[idx]
            if c == 't': return True, idx + 1
            if c == 'f': return False, idx + 1
            if c == '!':
                idx += 2  # skip '!('
                val, idx = parse(s, idx)
                return not val, idx + 1  # skip ')'
            # c is '&' or '|'
            op = c
            idx += 2  # skip op and '('
            vals = []
            while s[idx] != ')':
                if s[idx] == ',':
                    idx += 1
                    continue
                val, idx = parse(s, idx)
                vals.append(val)
            if op == '&':
                return all(vals), idx + 1
            else:
                return any(vals), idx + 1

        result, _ = parse(expression, 0)
        return result
        # Time: O(n)  Space: O(n)
# @lc code=end
