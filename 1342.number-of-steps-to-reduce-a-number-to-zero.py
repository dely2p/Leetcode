#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start
class Solution:
    def numberOfSteps (self, num: int) -> int:
        result = num
        cnt = 0
        while True:
            if result == 0:
                break
            if result % 2 == 0:
                result = result / 2
            else:
                result = result - 1
            cnt = cnt + 1
            print(result)

        return cnt
# @lc code=end

