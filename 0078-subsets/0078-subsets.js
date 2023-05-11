/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    const res = []
    function dfs(path, i) {
        if (i === nums.length) {
            res.push([...path])
            return
        }
        path.push(nums[i])
        dfs(path, i + 1)
        path.pop()
        dfs(path, i + 1)
    }
    dfs([], 0)
    return res
}