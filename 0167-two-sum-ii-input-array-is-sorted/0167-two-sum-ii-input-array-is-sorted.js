/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    const n = numbers.length
    
    let end = n - 1
    let beg = 0
    
    let res = []
    
    while (true) {
        const twoSum = numbers[end] + numbers[beg]
        
        if (twoSum === target) break
        if (twoSum < target) beg++
        if (twoSum > target) end--
    }
    
    return [beg + 1, end + 1]
};