/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    let memo = new Map()
    function dfs(prefix) {
        if (memo.has(prefix)) return memo.get(prefix)
        if (prefix === s) return true
        if (prefix.length >= s.length) return false
        if (prefix !== s.slice(0, prefix.length)) return false
        let res = false
        for (let word of wordDict) {
            const possible = dfs(prefix + word)
            memo.set(prefix + word, possible)
            res = res || possible
        }
        return res
    }
    return dfs('')
}