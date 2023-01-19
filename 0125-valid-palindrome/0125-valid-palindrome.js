/**
 * @param {string} s
 * @return {boolean}
 */

var preprocess = (s) => {
    s = s.toLowerCase()
    res = s.split('').filter(i => /[a-z|0-9]/.test(i))
    return res
}

var isPalindrome = function(s) {
    const processed = preprocess(s)
    
    let left = 0
    let right = processed.length - 1
    
    while (left < right) {
        if (processed[left] !== processed[right]) return false
        
        left++
        right--
    }
    
    return true
};