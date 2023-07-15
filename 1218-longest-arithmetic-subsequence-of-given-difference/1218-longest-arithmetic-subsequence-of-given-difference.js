/**
 * @param {number[]} arr
 * @param {number} difference
 * @return {number}
 */
var longestSubsequence = function(arr, difference) {
    const map = new Map()
    let maxLength = 1
    for (const num of arr) {
        const prev = num - difference
        if (map.has(prev)) {
            map.set(num, map.get(prev) + 1)
            maxLength = Math.max(maxLength, map.get(num))
        } else {
            map.set(num, 1)
        }
    }
    return maxLength
}