#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        while True:
            result = i * i
            if result > x:
                i = i-1
                break
            elif result == x:
                break
            i = i+1

        return i
# @lc code=end

