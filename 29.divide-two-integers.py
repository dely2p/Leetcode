#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = int(dividend/divisor)
        if abs(result) > 0xffffffff:
            return 0
        else:
            if dividend == -2147483648 and divisor == -1: # 이부분은 좀 더 생각해 볼 것
                return 2147483647
            return result
# @lc code=end

