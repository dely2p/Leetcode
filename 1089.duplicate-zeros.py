#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while True:
            if i >= len(arr):
                break
            if arr[i] == 0:
                arr[i+1:len(arr)] = arr[i:len(arr)-1]
                i = i + 2
            else:
                i = i + 1
            
        
# @lc code=end

