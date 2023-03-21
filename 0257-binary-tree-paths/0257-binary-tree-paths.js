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
 * @return {string[]}
 */
var binaryTreePaths = function(root) {
    let paths = []
    traverse(root, [], paths)
    return paths
}

var traverse = function(node, curPath, paths) {
    if (!node) return
    
    curPath.push(node.val)
    
    if (!node.left && !node.right) {
        paths.push(curPath.join('->'))
        curPath.pop()
        return
    }
    
    traverse(node.left, curPath, paths)
    traverse(node.right, curPath, paths)
    
    curPath.pop()
}