/**
 * @param {string} s
 * @return {boolean}
 */

var preprocess = function(s) {
    s = s.toLowerCase().split('')
    s = s.filter(chr => /[a-z0-9]/.test(chr))
    return s
}

var isPalindrome = function(s) {   
    const pStr = preprocess(s)
    
    let left = 0
    let right = pStr.length - 1
    
    while (left <= right) {
        if (pStr[left] !== pStr[right]) return false
        left++
        right--
    }
    
    return true
}