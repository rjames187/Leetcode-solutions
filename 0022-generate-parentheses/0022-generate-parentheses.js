/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    let res = []
    var dfs = function(comb, res, openCount, closeCount) {
        if (openCount >= n && closeCount >= n) {
            res.push(comb.join(''))
        }
        
        if (openCount < n) {
            comb.push('(')
            dfs(comb, res, openCount + 1, closeCount)
            comb.pop()
        }
        
        if (closeCount < openCount) {
            comb.push(')')
            dfs(comb, res, openCount, closeCount + 1)
            comb.pop()
        }
    }
    dfs([], res, 0, 0)
    return res
}