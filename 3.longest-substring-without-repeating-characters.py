#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStringList = [[]]
        maxLength = 0
        for i in range(0, len(s)):
            list = []
            for j in range(i, len(s)):
                if s[j] in list:
                    break
                list.append(s[j])
                subStringList.append(list)

        for item in subStringList:
            if maxLength < len(item):
                maxLength = len(item)
            
        return maxLength

# @lc code=end

