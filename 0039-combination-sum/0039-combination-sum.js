/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const res = []
    candidates.sort()
    function dfs (path, remaining, start) {
        if (remaining < 0) return
        if (remaining === 0) {
            res.push([...path])
            return
        }
        for (let i = start; i < candidates.length; i++) {
            if (i > 0 && candidates[i - 1] === candidates[i]) continue
            path.push(candidates[i])
            dfs (path, remaining - candidates[i], i)
            path.pop()
        }
    }
    dfs([], target, 0)
    return res
}