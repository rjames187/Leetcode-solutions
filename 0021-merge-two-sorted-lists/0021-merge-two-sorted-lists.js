/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var selectNewNode = (list1, list2) => {
    
    if (!list1) {
        return [2, new ListNode(list2.val)]
    } else if (!list2 || list1.val < list2.val) {
        return [1, new ListNode(list1.val)]
    } else {
        return [2, new ListNode(list2.val)]
    }
}

var mergeTwoLists = function(list1, list2) {
    if (!list1 && !list2) return null
    if (!list1) return list2
    if (!list2) return list1
    
    let firstData = selectNewNode(list1, list2)
    if (firstData[0] === 1) list1 = list1.next
    if (firstData[0] === 2) list2 = list2.next
    let newHead = firstData[1]
    let curNode = newHead
    
    while (list1 || list2) {
        const data = selectNewNode(list1, list2)
        
        if (data[0] === 1) list1 = list1.next
        if (data[0] === 2) list2 = list2.next
        
        curNode.next = data[1]
        curNode = curNode.next
    }
    
    return newHead
}