/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

var checkBalance = function(root) {
    if (!root) return [0, true]
    
    const [leftHeight, leftBalanced] = checkBalance(root.left)
    const [rightHeight, rightBalanced] = checkBalance(root.right)
    
    if (!leftBalanced || !rightBalanced) return [null, false]
    
    const thisBalanced = Math.abs(rightHeight - leftHeight) <= 1
    if (!thisBalanced) return [null, false]
    
    return [Math.max(rightHeight, leftHeight) + 1, true]
}

var isBalanced = function(root) {
    const [height, balanced] = checkBalance(root)
    return balanced
}