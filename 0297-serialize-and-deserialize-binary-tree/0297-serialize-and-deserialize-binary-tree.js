/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

var serializeDfs = function(root, nodes) {
    if (!root) {
        nodes.push('x')
        return
    }
    
    nodes.push(root.val)
    serializeDfs(root.left, nodes)
    serializeDfs(root.right, nodes)
}

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    const nodes = []
    serializeDfs(root, nodes)
    return nodes.join(' ')
}

var deserializeDfs = function(nodes) {
    const curVal = nodes.shift()
    if (curVal === 'x') return null
    
    const root = new TreeNode(curVal)
    
    root.left = deserializeDfs(nodes)
    root.right = deserializeDfs(nodes)
    
    return root
}

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    let nodes = data.split(' ')
    const root = deserializeDfs(nodes)
    return root
}

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */