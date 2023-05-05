/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
    function isValTwoDigit(s) {
        const num = Number(s)
        return num <= 26 && num >= 10
    }
    const memo = new Map()
    function dfs(startIndex) {
        if (startIndex >= s.length) return 1
        if (memo.has(startIndex)) return memo.get(startIndex)
        let numWays = 0
        if (s[startIndex] !== '0') numWays += dfs(startIndex + 1)
        if (startIndex < s.length - 1 && isValTwoDigit(s.slice(startIndex, startIndex + 2))) {
            numWays += dfs(startIndex + 2)
        }
        memo.set(startIndex, numWays)
        return numWays
    }
    return dfs(0)
}