#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        result = -1
        for index, num in enumerate(nums):
            if num >= target:
                result = index
                break
        
        if result == -1:
            return len(nums)
        return index

# @lc code=end

