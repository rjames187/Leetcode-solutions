/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    const min = Math.min(p.val, q.val)
    const max = Math.max(p.val, q.val)
    
    const isBetween = root.val >= min && root.val <= max
    if (isBetween) return root
    
    let result
    
    const isAbove = root.val > max
    if (isAbove) result = lowestCommonAncestor(root.left, p, q)
    else result = lowestCommonAncestor(root.right, p, q)
    
    return result
}