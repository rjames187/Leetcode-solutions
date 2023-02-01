/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    while (nums.length > 0) {
        let cur = nums.pop()
        if (nums.includes(cur)) return true
    }
    return false
}