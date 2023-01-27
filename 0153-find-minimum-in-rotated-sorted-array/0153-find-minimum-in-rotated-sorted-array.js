/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let left = 0
    let right = nums.length - 1
    let boundary = right
    let min = nums[right]
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        
        if (nums[mid] <= min) {
            boundary = mid
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    
    return nums[boundary]
};