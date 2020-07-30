#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        result = 0

        for v in nums:
            if v in dic.keys():
                dic[v] = dic[v] + 1
            else:
                dic[v] = 1

        for k in dic.keys():
            if dic[k] == 1:
                result = k
                break
            
        return result

# @lc code=end

