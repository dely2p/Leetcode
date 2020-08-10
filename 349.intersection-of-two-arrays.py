#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums1) < len(nums2):
            numA = nums2
            numB = nums1
        else:
            numA = nums1
            numB = nums2
        
        result = []
        for i in range(0,len(numA)):
            if numA[i] in numB and numA[i] not in result:
                result.append(numA[i])

        return result
# @lc code=end

