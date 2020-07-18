#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        width = (j-i) * min(height[i], height[j])
        while i < j:
            if height[i] <= height[j]:
                i = i + 1
            else:
                j = j - 1

            width = max(width, (j-i) * min(height[i], height[j]))

        return width

# @lc code=end

