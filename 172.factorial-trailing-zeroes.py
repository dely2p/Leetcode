#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        while n:
            cnt = cnt + int(n / 5)
            n = int(n / 5)
        return cnt
            
# @lc code=end

