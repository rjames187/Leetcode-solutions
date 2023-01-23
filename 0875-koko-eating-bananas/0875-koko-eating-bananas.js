/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var okayEatingSpeed  = (piles, h, k) => {
    let totalHours = 0
    for (let i = 0; i < piles.length; i++) {
        totalHours += Math.ceil(piles[i] / k)
        if (totalHours > h) return false
    }
    return true
}

var minEatingSpeed = function(piles, h) {
    leftK = 1
    rightK = Math.max(...piles)
    boundaryK = rightK
    
    while (leftK <= rightK) {
        const midK = Math.floor((leftK + rightK) / 2)
        
        if (okayEatingSpeed(piles, h, midK)) {
            boundaryK = midK
            rightK = midK - 1
        }
        else {
            leftK = midK + 1
        }
    }
    
    return boundaryK
}

// time: O(n log n) + O(n)
// space: O(1)