#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#
# PROBLEM:
# Given the heads of two linked lists, return the node where they intersect.
# If they don't intersect, return null. Lists must NOT be modified.
# The intersection is by reference, not value.
#
# APPROACH: Two pointer trick.
# Pointer A: traverse listA then listB.
# Pointer B: traverse listB then listA.
# If they intersect, they'll meet at the intersection after traversing same total distance.
# If no intersection, both reach null simultaneously.
# Why: both pointers travel (lenA + lenB) total — so they sync up.

# @lc code=start
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB   # switch lists when exhausted
            b = b.next if b else headA
        return a   # either the intersection node or null
        # Time: O(m+n)  Space: O(1)
# @lc code=end
