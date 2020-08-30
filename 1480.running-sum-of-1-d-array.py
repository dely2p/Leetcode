#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        list = []
        for i,v in enumerate(nums):
            tmp = 0
            for w in nums[0:i+1]:
                tmp = tmp + w
            list.append(tmp)

        return list
# @lc code=end

