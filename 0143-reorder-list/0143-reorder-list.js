/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    // construct list traversable in both directions
    let pointer = head
    let nodeList = []
    
    while (pointer) {
        nodeList.push(pointer)
        pointer = pointer.next
    }
    
    // construct new reordered list
    let newHead = nodeList.shift()
    let left = 0
    let right = nodeList.length - 1
    
    let curNode = newHead
    while (true) {
        let newNode = nodeList.pop()
        if (!newNode) return newHead
        newNode.next = null
        curNode.next = newNode
        curNode = curNode.next
        
        newNode = nodeList.shift()
        if (!newNode) return newHead
        newNode.next = null
        curNode.next = newNode
        curNode = curNode.next
    }
};