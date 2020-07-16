#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
import sys
class Solution:
    def reverse(self, x: int) -> int:
        val = ""
        result = ""
        positiveNumber = False

        if x < 0:
            val = str(-x)
            positiveNumber = False
        else:
            val = str(x)
            positiveNumber = True

        print(val)

        result = val[::-1]
        print(result)

        if positiveNumber is not True: #음수
            print(int(result))
            result = int(result) * -1
        else:
            print(int(result))
            result = int(result)

        print(-sys.maxsize - 1)
        print(sys.maxsize)

        if result > -2147483648 and result < 2147483648:
            return result
        else:
            return 0
        
# @lc code=end

