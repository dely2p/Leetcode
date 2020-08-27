#
# @lc app=leetcode id=1394 lang=python3
#
# [1394] Find Lucky Integer in an Array
#

# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = {}
        result = -1
        for v in arr:
            if v in dic:
                dic[v] = dic[v] + 1
            else:
                dic[v] = 1

        dicToList = list(dic.keys())
        dicToList.sort(reverse=True)
        print(dicToList)
        for k in dicToList:
            if k == dic[k]:
                result = k
                break

        return result
# @lc code=end

