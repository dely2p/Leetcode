#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bank = [0,0,0,0] # 5, 10, not, 20
        result = True
        for bill in bills:
            if bill == 10:
                bank[0] = bank[0] - 1
                if bank[0] < 0:
                    result = False
                    break
            elif bill == 20:
                bank[0] = bank[0] - 1
                bank[1] = bank[1] - 1
                if bank[0] < 0 or bank[1] < 0:
                    bank[0] = bank[0] + 1
                    bank[1] = bank[1] + 1
                    bank[0] = bank[0] - 3
                    if bank[0] < 0 or bank[1] < 0:
                        result = False
                        break
            
            bank[int(bill/5-1)] = bank[int(bill/5-1)] + 1
            print(bill, bank[0], bank[1], bank[3])
            
        return result
# @lc code=end

