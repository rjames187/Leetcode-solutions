/**
 * @param {string[]} strs
 * @return {string[][]}
 */

var groupAnagrams = function(strs) {
    const map = new Map()
    
    for (let str of strs) {
        const reordered = str.split('').sort().join('')
        
        const group = map.get(reordered) || []
        group.push(str)
        map.set(reordered, group)
    }
    
    return Array.from(map.values())
}