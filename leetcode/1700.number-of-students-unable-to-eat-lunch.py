#
# @lc app=leetcode id=1700 lang=python
#
# [1700] Number of Students Unable to Eat Lunch
#
# PROBLEM:
# Students stand in a queue. Sandwiches are stacked. Student at front either
# takes the top sandwich (if preferred) or goes to back of queue.
# Return number of students who can't eat.
# Example: students=[1,1,0,0], sandwiches=[0,1,0,1] → 0
#
# APPROACH: Count how many students want 0s and 1s.
# Walk through sandwich stack. If no student wants the top sandwich, stop.

# @lc code=start
class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = [0, 0]
        for s in students:
            count[s] += 1

        for sandwich in sandwiches:
            if count[sandwich] == 0:
                # No one wants this — everyone remaining can't eat
                return count[0] + count[1]
            count[sandwich] -= 1

        return 0
        # Time: O(n)  Space: O(1)
# @lc code=end
