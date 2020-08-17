#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        result = False
        power = 1
        if n == 1:
            return True
        while True:
            power = 2 * power
            if power == n:
                result = True
                break
            elif power > n:
                break

        return result

            
# @lc code=end

