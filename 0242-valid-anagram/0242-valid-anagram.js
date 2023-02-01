/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

var isAnagram = function(s, t) {
    let frequencyMap = new Map()
    
    for (let val of s) editMap(frequencyMap, val, false)
    for (let val of t) editMap(frequencyMap, val, true)
    
    return allZeros(frequencyMap)
}

var editMap = function(map, val, neg) {
    let addend = neg ? -1 : 1
    if (map.has(val)) {
        const cur = map.get(val)
        map.set(val, cur + addend)
    }
    else map.set(val, addend)
}

var allZeros = function(map) {
    for (val of map.values()) {
        if (val !== 0) return false
    }
    return true
}


