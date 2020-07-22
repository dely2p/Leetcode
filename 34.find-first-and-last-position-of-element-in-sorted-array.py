#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        for index, num in enumerate(nums):
            if num == target:
                result.append(index)
        
        if result == []:
            return [-1, -1]
        return [result[0], result[-1]]
# @lc code=end

