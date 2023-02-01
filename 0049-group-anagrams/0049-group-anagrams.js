/**
 * @param {string[]} strs
 * @return {string[][]}
 */

var groupAnagrams = function(strs) {
    const map = new Map()
    
    for (let str of strs) {
        const key = reorder(str)
        const vals = map.get(key) || []
        vals.push(str)
        map.set(key, vals)
    }
    
    return Array.from(map.values())
}

var reorder = function(str) {
    return str.split('').sort().join('')
}