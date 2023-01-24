/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    let left = 0
    let right = x
    let boundary = 0
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        const square = mid ** 2
        
        if (square === x) return mid
        if (square > x) right = mid - 1
        if (square < x) {
            boundary = mid
            left = mid + 1
        }
    }
    
    return boundary
}