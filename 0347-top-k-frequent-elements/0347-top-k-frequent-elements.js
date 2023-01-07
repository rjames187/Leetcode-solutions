/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

var addToMap = function(map, item) {
    if (map.has(item)) {
        const curVal = map.get(item)
        map.set(item, curVal + 1)
    } else {
        map.set(item, 1)
    }
}

var topKFrequent = function(nums, k) {
    let counter = new Map()
    
    for (num of nums) {
        addToMap(counter, num)
    }
    
    let keys = Array.from(counter.keys())
    // sorts the keys of the counter map by their values in descending order
    keys.sort((a, b) => counter.get(b) - counter.get(a))
    
    return keys.slice(0, k)
};