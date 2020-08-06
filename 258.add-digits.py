#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        sum = num
        result = 0
        while True:
            strNum = str(sum)
            sum = 0
            for c in strNum:
                print(c)
                sum = sum + int(c)

            if sum < 10:
                result = sum
                break

        return result

# @lc code=end

