#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        list = s.split(" ")
        print(list)

        for i,w in enumerate(list):
            result = result + w[::-1]
            if i < len(list)-1:
                result = result + " "

        return result
# @lc code=end

