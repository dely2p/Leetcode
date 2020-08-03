#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        max = 0
        result = 0
        for v in nums:
            if v in dic:
                dic[v] = dic[v] + 1
            else:
                dic[v] = 1

        for k, v in dic.items():
            print(v)
            if max < v:
                max = v
                result = k

        return result
# @lc code=end

