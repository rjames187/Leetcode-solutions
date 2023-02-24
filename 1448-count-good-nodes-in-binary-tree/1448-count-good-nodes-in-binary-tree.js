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
    
    let thisCount = 1
    if (root.val > max) max = root.val
    else if (root.val < max) thisCount = 0
    
    const leftCount = countGoodNodes(root.left, max)
    const rightCount = countGoodNodes(root.right, max)
    
    return leftCount + rightCount + thisCount
}

var goodNodes = function(root) {
    return countGoodNodes(root, Number.NEGATIVE_INFINITY)
}