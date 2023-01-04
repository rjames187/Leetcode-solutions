/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */



var isAnagram = function(s, t) {
    let freqMap = new Map()

    var logOcc = function(chr, sign) {
        if (freqMap.has(chr)) {
            var curVal = freqMap.get(chr)
            freqMap.set(chr, curVal + sign)
            return
        }
        freqMap.set(chr, sign)
    }
    
    var onlyZeros = function(it) {
        for (i of it) {
            if (i !== 0) {
                return false
            }
        }
        return true
    }
    
    if (s.length !== t.length) { return false }
    for (let i = 0; i < s.length; i++) {
        logOcc(s[i], 1)
        logOcc(t[i], -1)
    }
    
    const mapIter = freqMap.values()
    return onlyZeros(mapIter)
};

// time: O(N)

