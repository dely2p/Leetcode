#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        list = [4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824]
        if num in list or num == 1:
            return True
        else:
            return False

# @lc code=end

