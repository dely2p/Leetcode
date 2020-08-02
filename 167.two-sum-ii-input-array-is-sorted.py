#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        list = []
        while True:
            if numbers[i] + numbers[j] == target:
                list.append(i+1)
                list.append(j+1)
                break
            elif numbers[i] + numbers[j] < target:
                i = i + 1
            elif numbers[i] + numbers[j] > target:
                j = j - 1

        return list

# @lc code=end

