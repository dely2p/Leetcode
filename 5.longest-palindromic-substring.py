#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        result = ""
        for i, v in enumerate(s):
            for j in range(i, len(s)):
                if v == s[j]:
                    subString = s[i:j+1]
                    if subString[::-1] == subString:
                        if len(result) < len(subString):
                            result = subString

        return result
                    
            
# @lc code=end

