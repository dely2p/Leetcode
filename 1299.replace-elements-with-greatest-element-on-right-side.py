#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        index = 0
        result = []
        for i,v in enumerate(arr):
            if i+1 == len(arr):
                result.append(-1)
                break
            result.append(max(arr[i+1:len(arr)]))
            index = index + 1

        return result
# @lc code=end

