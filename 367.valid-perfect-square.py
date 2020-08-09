#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        val = 1
        result = False
        while val < 808201:
            if num == val * val:
                result = True
                break
            val = val + 1

        return result
# @lc code=end

