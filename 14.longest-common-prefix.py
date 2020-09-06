#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return ""

        result = strs[0]
        for s in strs:
            temp = ""
            if len(s) > len(result):
                for i,v in enumerate(result):
                    if result[i] == s[i]:
                        temp = temp + result[i]
                    else:
                        break
            else:
                for i,v in enumerate(s):
                    if result[i] == s[i]:
                        temp = temp + result[i]
                    else:
                        break

            result = temp

        return result

# @lc code=end

