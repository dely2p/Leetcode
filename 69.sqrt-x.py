#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        v = 1
        result = 0
        while True:
            if v * v > x:
                result = v - 1
                break
            v = v + 1
        return result
# @lc code=end

