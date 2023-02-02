/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var calcMid = function(left, right) {
    return Math.floor((left + right) / 2)
}

var searchMatrix = function(matrix, target) {
    const n = matrix[0].length
    const m = matrix.length
    
    let left = 0
    let right = m - 1
    let boundary = right
    let mid = null
    
    while (left <= right) {
        mid = calcMid(left, right)
        
        if (matrix[mid][0] === target) return true
        if (matrix[mid][0] < target) {
            boundary = mid
            left = mid + 1
        }
        else right = mid - 1
    }
    
    const y = boundary
    console.log(y)
    
    left = 0
    right = n - 1
    
    while (left <= right) {
        mid = calcMid(left, right)
        
        if (matrix[y][mid] === target) return true
        if (matrix[y][mid] > target) right = mid - 1
        else left = mid + 1
    }
    
    return false
}