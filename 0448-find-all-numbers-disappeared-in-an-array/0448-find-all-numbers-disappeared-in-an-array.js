/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    const n = nums.length
    const left = new Set()
    for (let i = 1; i <= n; i++) {
        left.add(i)
    }
    
    for (const num of nums) {
        left.delete(num)
    }
    
    return Array.from(left.values())
}