#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        f = 1
        index = int((f+n)/2)
        while True:
            if f == n:
                result = index
                break
            if isBadVersion(index): #True
                if isBadVersion(index-1) == False:
                    result = index
                    break
                n = index
            else:
                if isBadVersion(index+1) == True:
                    result = index+1
                    break
                f = index
            index = int((f+n)/2)
            
        
        return result
# @lc code=end

