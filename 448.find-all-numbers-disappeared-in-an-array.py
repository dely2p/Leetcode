#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        list = [0] * len(nums)
        result = []
        for n in nums:
            list[n-1] = list[n-1] + 1
        
        for i, c in enumerate(list):
            if c == 0:
                result.append(i+1)

        return result
# @lc code=end

