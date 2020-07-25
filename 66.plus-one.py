#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        newDigits = digits[::-1]
        for index, num in enumerate(newDigits):
            result = result + (num * pow(10,index))

        result = result + 1
        list = []
        for index in range(len(str(result)), 0, -1):
            num = int(result / pow(10,index-1))
            result = int(result % pow(10,index-1))
            list.append(num)

        return list

# @lc code=end

