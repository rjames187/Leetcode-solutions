/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    const seen = new Map()
    const assigned = new Set()
    words = s.split(" ")
    if (words.length !== pattern.length) return false
    
    for (let i = 0; i < pattern.length; i++) {
        const chr = pattern[i]
        if (seen.has(chr)) {
            if (seen.get(chr) !== words[i]) return false
        } else {
            if (assigned.has(words[i])) return false
            seen.set(chr, words[i])
            assigned.add(words[i])
        }
    }
    
    return true
}