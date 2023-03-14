/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

var recurse = function(child, val) {
    return child ? insertIntoBST(child, val) : new TreeNode(val)
}

/**
 * @param {TreeNode} root
 * @param {number} val
 * @return {TreeNode}
 */
var insertIntoBST = function(root, val) {
    if (!root) return new TreeNode(val)
    
    if (root.val < val) root.right = recurse(root.right, val)
    else root.left = recurse(root.left, val)
    
    return root
}