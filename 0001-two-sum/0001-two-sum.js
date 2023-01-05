/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hash = new Map();
    
    for (let i = 0; i < nums.length; i++) {
        const difference = target - nums[i]
        if (hash.has(difference)) {
            return [i, hash.get(difference)]
        }
        hash.set(nums[i], i)
    }
    
    return "error"
};