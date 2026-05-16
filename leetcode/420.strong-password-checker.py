#
# @lc app=leetcode id=420 lang=python
#
# [420] Strong Password Checker (HARD)
#
# PROBLEM:
# A password is strong if: length 6-20, contains uppercase, lowercase, digit,
# and no 3+ consecutive repeating characters.
# Return minimum changes (insert/delete/replace) to make it strong.
#
# APPROACH: Complex greedy with case analysis for too short, too long, just right.
# Track missing categories and repeated sequences.

# @lc code=start
class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        n = len(password)
        missing = 3
        if any(c.islower() for c in password): missing -= 1
        if any(c.isupper() for c in password): missing -= 1
        if any(c.isdigit() for c in password): missing -= 1

        # Find repeating sequences of length >= 3
        repeats = []  # lengths of repeat groups
        i = 2
        while i < n:
            if password[i] == password[i-1] == password[i-2]:
                length = 2
                while i < n and password[i] == password[i-1]:
                    length += 1
                    i += 1
                repeats.append(length)
            else:
                i += 1

        if n < 6:
            return max(missing, 6 - n)

        if n <= 20:
            replace = sum(r // 3 for r in repeats)
            return max(missing, replace)

        # n > 20: need to delete (n - 20) characters
        to_delete = n - 20
        replace = 0
        rem1 = rem2 = 0

        # Optimize deletions by reducing repeats
        for r in repeats:
            if to_delete > 0 and r % 3 == 0:
                to_delete -= 1; r -= 1
        for i in range(len(repeats)):
            if to_delete > 0 and repeats[i] % 3 == 1:
                to_delete -= 2; repeats[i] -= 2
        for i in range(len(repeats)):
            if to_delete > 0:
                d = min(to_delete, repeats[i] - 2)
                repeats[i] -= d
                to_delete -= d

        replace = sum(r // 3 for r in repeats)
        return (n - 20) + max(missing, replace)
        # Time: O(n)  Space: O(n)
# @lc code=end
