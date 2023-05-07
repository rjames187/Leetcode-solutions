/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    const memo = new Map()
    function dfs(value) {
        if (value > amount) return Infinity
        if (value === amount) return 0
        if (memo.has(value)) return memo.get(value)
        let minNum = Infinity
        for (let coin of coins) {
            minNum = Math.min(minNum, dfs(value + coin) + 1)
        }
        memo.set(value, minNum)
        return minNum
    }
    const res = dfs(0)
    return res === Infinity ? -1 : res
}