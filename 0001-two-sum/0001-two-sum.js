/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let valToIndex = new Map()
    
    for (let i = 0; i < nums.length; i++) {
        const curVal = nums[i]
        if (valToIndex.has(target - curVal)) return [i, valToIndex.get(target - curVal)]
        valToIndex.set(curVal, i)
    }
}