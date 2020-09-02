#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        s = str(bin(n))
        print(s)
        
        cnt = 0
        for v in s:
            if v == "1":
                cnt = cnt + 1

        return cnt
# @lc code=end

