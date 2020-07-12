#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list = nums1 + nums2
        list.sort()
        mid = int(len(list)/2)
        if len(list)%2 == 0: #짝수
            return (list[mid-1] + list[mid]) / 2
        else: #홀수
            return list[mid]


# @lc code=end

