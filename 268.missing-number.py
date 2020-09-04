#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        index = 0
        result = 0
        nums.sort()
        for i in range(0,len(nums)+1):
            if i >= len(nums) or nums[i] != index:
                result = index
                break
            index = index + 1
        return result
# @lc code=end

