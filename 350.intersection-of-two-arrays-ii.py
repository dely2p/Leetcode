#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for v in nums1:
            if v in nums2:
                result.append(v)
                nums2.remove(v)
        return result

# @lc code=end

