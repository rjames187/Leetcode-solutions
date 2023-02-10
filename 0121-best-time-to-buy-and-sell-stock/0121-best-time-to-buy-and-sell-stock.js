/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxProfit = 0
    
    let left = 0, right = 1
    
    while (right < prices.length) {
        const profit = prices[right] - prices[left]
        
        maxProfit = Math.max(maxProfit, profit)
        
        if (profit < 0) left = right
        right++
    }
    
    return maxProfit
}