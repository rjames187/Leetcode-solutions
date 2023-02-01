/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

var reorder = function(str) {
    return str.split('').sort().join('')
}

var isAnagram = function(s, t) {
    return reorder(s) === reorder(t)
}


