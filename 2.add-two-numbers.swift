/*
 * @lc app=leetcode id=2 lang=swift
 *
 * [2] Add Two Numbers
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        var node1: ListNode? = l1
        var node2: ListNode? = l2
        var storedValue: Int = 0
        var currentNode = ListNode()
        let resultNode = currentNode
        var isContinue: Bool = true
        while isContinue {
            var sum = (node1?.val ?? 0) + (node2?.val ?? 0) + storedValue
            if sum >= 10 {
                storedValue = sum / 10
                sum = sum - 10
            }else { storedValue = 0 }
            currentNode.val = sum
            
            if node1?.next == nil, node2?.next == nil, storedValue == 0 { isContinue = false; break }
            
            let newNode = ListNode()
            currentNode.next = newNode
            currentNode = currentNode.next!
            
            if let n1 = node1?.next { node1 = n1 }
            else { node1 = nil }
            if let n2 = node2?.next { node2 = n2 }
            else { node2 = nil }
        }
        return resultNode
    }
}
// @lc code=end

