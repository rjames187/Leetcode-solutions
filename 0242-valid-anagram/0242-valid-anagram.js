/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */



var isAnagram = function(s, t) {
    let freq_map = new Map()

    var log_occ = function(chr, sign) {
        if (freq_map.has(chr)) {
            var cur_val = freq_map.get(chr)
            freq_map.set(chr, cur_val + sign)
            return
        }
        freq_map.set(chr, sign)
    }
    
    if (s.length !== t.length) { return false }
    for (let i = 0; i < s.length; i++) {
        log_occ(s[i], 1)
        log_occ(t[i], -1)
    }
    
    return Array.from(freq_map.values()).every(i => i === 0)
};

// time: O(N)

