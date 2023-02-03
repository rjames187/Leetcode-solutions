/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var isInLeftPortion = function(midVal, leftVal) {
    return midVal >= leftVal
}

var search = function(nums, target) {
    let left = 0
    let right = nums.length - 1
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        
        if (nums[mid] === target) return mid
        
        if (isInLeftPortion(nums[mid], nums[left])) {
            if (target > nums[mid] || target < nums[left]) left = mid + 1
            else right = mid - 1
        }
        else {
            if (target < nums[mid] || target > nums[right]) right = mid - 1
            else left = mid + 1
        }
    }
    
    return -1
}
