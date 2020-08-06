#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        list = {}
        result = []
        for v in nums:
            if v in list:
                list[v] = list[v] + 1
            else:
                list[v] = 1
        
        for key,value in list.items():
            if value == 1:
                result.append(key)

        return result
# @lc code=end

