#
# @lc app=leetcode id=726 lang=python
#
# [726] Number of Atoms (HARD)
#
# PROBLEM:
# Given a chemical formula, return the count of each atom in sorted order.
# Example: formula="H2O" → "H2O"  ;  formula="Mg(OH)2" → "H2MgO2"
#
# APPROACH: Stack-based parsing.
# Parse left-to-right: push new dict on '(', on ')' pop and multiply by number,
# merge result into top of stack.

# @lc code=start
from collections import defaultdict

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stack = [defaultdict(int)]
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                # Read multiplier
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                mult = int(formula[start:i]) if i > start else 1
                top = stack.pop()
                for atom, cnt in top.items():
                    stack[-1][atom] += cnt * mult
            elif formula[i].isupper():
                # Read element name
                start = i; i += 1
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[start:i]
                # Read count
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                cnt = int(formula[start:i]) if i > start else 1
                stack[-1][atom] += cnt
            else:
                i += 1

        counts = stack[0]
        return ''.join(atom + (str(cnt) if cnt > 1 else '')
                       for atom, cnt in sorted(counts.items()))
        # Time: O(n^2) worst case  Space: O(n)
# @lc code=end
