/**
 * @param {number[]} height
 * @return {number}
 */

var calcArea = function(i, j, height) {
    const w = j - i
    const h = Math.min(height[i], height[j])
    return w * h
}

var maxArea = function(height) {
    let biggestArea = Number.NEGATIVE_INFINITY
    
    let left = 0
    let right = height.length - 1
    
    while (left < right) {
        const curArea = calcArea(left, right, height)
        biggestArea = Math.max(curArea, biggestArea)
        
        if (height[left] > height[right]) right--
        else left++
    }
    
    return biggestArea
}