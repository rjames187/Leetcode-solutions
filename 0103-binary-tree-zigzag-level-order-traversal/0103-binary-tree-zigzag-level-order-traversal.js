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
 * @return {number[][]}
 */
var zigzagLevelOrder = function(root) {
    if (!root) return []
    const res = []
    const queue = [root]
    let reverse = false
    while (queue.length) {
        const level = []
        const numInLevel = queue.length
        for (let i = 0; i < numInLevel; i++) {
            const node = queue.shift()
            if (reverse) level.unshift(node.val)
            else level.push(node.val)
            if (node.left) queue.push(node.left)
            if (node.right) queue.push(node.right)
        }
        reverse = !reverse
        res.push(level)
    }
    return res
}