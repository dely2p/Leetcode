#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = 100
        for v in nums:
            if v < minVal:
                minVal = v

        return minVal
# @lc code=end

