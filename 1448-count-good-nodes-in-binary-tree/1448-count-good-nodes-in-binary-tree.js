/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var countGoodNodes = function(root, max) {
    if (!root) return 0
    
    const thisCount = root.val >= max ? 1 : 0
    max = Math.max(root.val, max)
    
    const leftCount = countGoodNodes(root.left, max)
    const rightCount = countGoodNodes(root.right, max)
    
    return leftCount + rightCount + thisCount
}

var goodNodes = function(root) {
    return countGoodNodes(root, Number.NEGATIVE_INFINITY)
}