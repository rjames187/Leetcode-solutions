/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    const res = []
    candidates.sort((a, b) => b - a)
    function dfs(path, remaining, start) {
        if (remaining < 0) return
        if (remaining === 0) {
            res.push([...path])
            return
        }
        for (let i = start; i < candidates.length; i++) {
            if (i > start && candidates[i] === candidates[i - 1]) continue
            path.push(candidates[i])
            dfs(path, remaining - candidates[i], i + 1)
            path.pop()
        }
    }
    dfs([], target, 0)
    return res
}