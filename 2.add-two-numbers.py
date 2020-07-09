#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        storedValue = 0
        currentNode = ListNode()
        resultNode = currentNode
        isContinue = True
        while isContinue:
            sum = l1.val + l2.val + storedValue
            if sum >= 10:
                storedValue = sum / 10
                sum = sum - 10
            else:
                storedValue = 0
            currentNode.val = int(sum)
            
            if (l1.next is None) and (l2.next is None) and (storedValue == 0):
                isContinue = False
                break
            
            newNode = ListNode()
            currentNode.next = newNode
            currentNode = currentNode.next
            
            if l1.next is not None:
                l1 = l1.next
            else:
                l1.val = 0
            if l2.next is not None:
                l2 = l2.next
            else:
                l2.val = 0

        return resultNode
# @lc code=end

