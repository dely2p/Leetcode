#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        result = ""
        for i, l in enumerate(letters):
            if l<=target:
                if i == len(letters)-1:
                    result = letters[0]
                    break
                continue
            else:
                result = l
                break

        return result
# @lc code=end

