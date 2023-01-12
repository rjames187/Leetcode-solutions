/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    let set = new Set(nums)
    let maxStreak = 0
    
    for (let num of [... set]) {
        const prevNum = num - 1
        if (set.has(prevNum)) continue
        
        
        let conseqNums = 0
        let curNum = num
        while (set.has(curNum)) {
            conseqNums += 1
            curNum += 1
        }
        
        maxStreak = Math.max(conseqNums, maxStreak)
    }
    
    return maxStreak
};