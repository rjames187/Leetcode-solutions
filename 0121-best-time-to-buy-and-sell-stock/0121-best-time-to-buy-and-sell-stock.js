/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
   let left = 0
   let right = 1
   let maxProfit = 0
   
   while (right < prices.length) {
       const profit = prices[right] - prices[left]
       
       if (profit < 0) left = right
       else maxProfit = Math.max(maxProfit, profit)
       
       right++
   }
    
    return maxProfit
}