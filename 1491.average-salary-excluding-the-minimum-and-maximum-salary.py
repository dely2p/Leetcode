#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#

# @lc code=start
class Solution:
    def average(self, salary: List[int]) -> float:
        list = []
        list.append(max(salary))
        list.append(min(salary))
        
        sum = 0
        result = 0

        for v in salary:
            if v not in list:
                sum = sum + v
                
        result = sum / (len(salary)-2)
        return result

# @lc code=end

