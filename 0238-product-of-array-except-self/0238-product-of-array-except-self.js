/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    if (nums.length <= 1) { return nums }
    
    let res = new Array(nums.length).fill(1)
    
    let prev = nums[0]
    
    for (let i = 1; i < nums.length; i++) {
        res[i] *= prev
        prev *= nums[i]
    }
    
    prev = nums[nums.length - 1]
    
    for (let j = nums.length - 2; j >= 0; j--) {
        res[j] *= prev
        prev *= nums[j]
    }
    
    return res
};