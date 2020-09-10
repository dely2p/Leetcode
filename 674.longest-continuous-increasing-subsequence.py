#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cnt = 0
        tmp = 0
        maxCnt = 0
        for v in nums:
            if v > tmp:
                cnt = cnt + 1
            else:
                if cnt > maxCnt:
                    maxCnt = cnt
                cnt = 1
            tmp = v
        if cnt > maxCnt:
            maxCnt = cnt
        return maxCnt
# @lc code=end

