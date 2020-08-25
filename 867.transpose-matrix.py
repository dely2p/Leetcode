#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

# @lc code=start
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for i,v in enumerate(A[0]):
            temp = []
            for j,w in enumerate(A):
                temp.append(A[j][i])
            result.append(temp)

        return result
# @lc code=end

