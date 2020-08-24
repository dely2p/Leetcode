#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for n in nums:
            length = len(str(n))
            if length%2 == 0:
                cnt = cnt + 1

        return cnt
# @lc code=end

