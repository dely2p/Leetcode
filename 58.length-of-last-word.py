#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start = 0
        end = 0
        isFirstWord = True
        for i, v in enumerate(s):
            if v is not ' ':
                if isFirstWord:
                    start = i
                    end = i+1
                    isFirstWord = False
                else:
                    end = i+1
            else: # ' ' 일 때
                isFirstWord = True

        return len(s[start:end])

# @lc code=end

