#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        list = {}
        result = False
        for i, v in enumerate(nums):
            if v in list:
                length = i - list[v]
                if length <= k:
                    result = True
                    break
            list[v] = i

        return result
            
# @lc code=end

