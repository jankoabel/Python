#
# @lc app=leetcode id=2637 lang=python
#
# [2637] Promise Time Limit (JavaScript problem — Python equivalent concept)
#
# NOTE: This is a JavaScript-only LeetCode problem. Below is the Python equivalent
# of the concept: a timeout wrapper using threading.
#
# PROBLEM:
# Given an async function fn and a time limit t (ms), return a wrapped version
# that rejects with "Time Limit Exceeded" if fn takes longer than t ms.
#
# APPROACH (Python threading concept):
# Run fn in a thread. Join with timeout. If not done in time, raise exception.

# @lc code=start
import threading

def time_limited(fn, t_ms):
    """Wraps fn to raise TimeoutError if it exceeds t_ms milliseconds."""
    def wrapper(*args, **kwargs):
        result = [None]
        error  = [None]

        def target():
            try:
                result[0] = fn(*args, **kwargs)
            except Exception as e:
                error[0] = e

        thread = threading.Thread(target=target)
        thread.start()
        thread.join(timeout=t_ms / 1000.0)

        if thread.is_alive():
            raise TimeoutError("Time Limit Exceeded")
        if error[0]:
            raise error[0]
        return result[0]

    return wrapper
    # Time: O(1) overhead  Space: O(1)
# @lc code=end
