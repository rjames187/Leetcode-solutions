/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    if (s.length < 2) return s.length
    
    const set = new Set()
    
    let maxLength = 0
    
    let right = 0
    let left = 0
    
    while (right < s.length) {
        const rVal = s.charAt(right)
        
        if (set.has(rVal)) {
            while (s.charAt(left) !== rVal) {
                set.delete(s.charAt(left))
                left++
            }
            set.delete(s.charAt(left))
            left++
        }
        
        maxLength = Math.max(maxLength, right - left + 1)
        set.add(rVal)
        right++
    }
    
    return maxLength
}