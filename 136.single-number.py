#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0
        list = []
        for i, v in enumerate(nums):
            if v in list:
                list.remove(v)
            else:
                list.append(v)
        
        return list[0]
            

# @lc code=end

