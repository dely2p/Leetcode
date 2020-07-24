#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        result = 1
        numList = sorted(nums)
        print(numList)
        for num in numList:
            if num == result:
                result = result + 1
                print(result)

        return result
# @lc code=end

