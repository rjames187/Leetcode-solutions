/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */

var getNewPointer = function(hash_map, oldNode) {
    if (!oldNode) return null
    if (hash_map.has(oldNode)) {
        return hash_map.get(oldNode)
    }
   let newNode = new ListNode(oldNode.val)
    hash_map.set(oldNode, newNode)
    return newNode
}

var copyRandomList = function(head) {
    if (!head) return null
    
    hash_map = new Map()
    
    const copyHead = new ListNode(head ? head.val : null)
    
    let oldPointer = head
    let newPointer = copyHead
    
    hash_map.set(head, copyHead)
    
    while (oldPointer) {
        newPointer.random = getNewPointer(hash_map, oldPointer.random)
        newPointer.next = getNewPointer(hash_map, oldPointer.next)
        
        oldPointer = oldPointer.next
        newPointer = newPointer.next
    }
    
    return copyHead
}