#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        list = {}
        result = False
        for v in nums:
            if v in list:
                result = True
                break
            else:
                list[v] = 1
            
        return result
# @lc code=end

