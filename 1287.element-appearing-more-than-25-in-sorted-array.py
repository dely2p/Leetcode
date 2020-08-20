#
# @lc app=leetcode id=1287 lang=python3
#
# [1287] Element Appearing More Than 25% In Sorted Array
#

# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        list = {}
        result = 0
        max = 0
        for v in arr:
            if v in list:
                list[v] = list[v] + 1
            else:
                list[v] = 1
            
        for k,v in list.items():
            if v > max:
                result = k
                max = v

        return result


# @lc code=end

