/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    const nonRepeating = new Set()
    const indexMap = new Map()
    for (let i = 0; i < s.length; i++) {
        const chr = s[i]
        if (indexMap.has(chr)) {
            nonRepeating.delete(chr)
        } else {
            nonRepeating.add(chr)
            indexMap.set(chr, i)
        }
    }
    if (nonRepeating.size < 1) return -1
    let res = Infinity
    for (const chr of nonRepeating.values()) {
        const i = indexMap.get(chr)
        res = Math.min(res, i)
    }
    return res
}