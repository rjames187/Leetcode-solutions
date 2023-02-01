/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let set = new Set()
    for (val of nums) {
        if (set.has(val)) return true
        set.add(val)
    }
    return false
}