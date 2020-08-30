#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        arr = nums[::-1]
        return (arr[0]-1) * (arr[1]-1)
            
# @lc code=end

