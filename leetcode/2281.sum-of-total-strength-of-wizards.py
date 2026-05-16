#
# @lc app=leetcode id=2281 lang=python
#
# [2281] Sum of Total Strength of Wizards (HARD)
#
# PROBLEM:
# Strength of a group = min(strength) * sum(strength) of all contiguous wizards.
# Return sum over all groups, modulo 10^9+7.
# Example: strength=[1,3,1,2] → 44
#
# APPROACH: Monotonic stack for contribution of each element as minimum.
# For each element as min, find the left/right boundary using stack.
# Use prefix sums of prefix sums (double prefix) for range sum calculations.

# @lc code=start
class Solution(object):
    def totalStrength(self, strength):
        """
        :type strength: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(strength)
        # prefix[i] = sum(strength[0..i-1])
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + strength[i]
        # prefix2[i] = sum(prefix[0..i-1]) = sum of prefix sums
        prefix2 = [0] * (n + 2)
        for i in range(n + 1):
            prefix2[i+1] = prefix2[i] + prefix[i]

        stack = []  # monotonic stack (increasing)
        result = 0

        def range_sum(l, r):
            # sum of strength[l..r]
            return prefix[r+1] - prefix[l]

        def prefix_sum_range(l, r):
            # sum of prefix[l..r+1] = prefix2[r+2] - prefix2[l]
            return prefix2[r+2] - prefix2[l]

        for i in range(n + 1):
            while stack and (i == n or strength[stack[-1]] >= strength[i]):
                mid = stack.pop()
                l = stack[-1] + 1 if stack else 0
                r = i - 1

                # sum over all subarrays with min at mid:
                # sum = sum_{a=l}^{mid} sum_{b=mid}^{r} strength[mid] * sum(strength[a..b])
                # = strength[mid] * (sum_{a=l}^{mid} (sum of prefix[mid+1..r+1] - prefix[a..mid]))
                # Simplified using double prefix sums:
                left_contrib  = prefix_sum_range(l, mid) - prefix_sum_range(0, l-1) if l > 0 else prefix_sum_range(0, mid)
                right_contrib = prefix_sum_range(mid, r) if mid <= r else 0

                # Simpler direct formula:
                # contribution = strength[mid] * (
                #   (mid-l+1)*prefix_sum_range(mid,r) - (r-mid+1)*prefix_sum_range(l-1,mid-1)
                # )
                r_sum = prefix2[r+2] - prefix2[mid+1]  # sum of prefix[mid+1..r+1]
                l_sum = prefix2[mid+1] - prefix2[l]    # sum of prefix[l..mid]
                contrib = (strength[mid] * ((mid - l + 1) * r_sum - (r - mid + 1) * l_sum)) % MOD
                result = (result + contrib) % MOD

            if i < n:
                stack.append(i)

        return result
        # Time: O(n)  Space: O(n)
# @lc code=end
