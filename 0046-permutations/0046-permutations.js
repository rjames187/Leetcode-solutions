/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    const res = []
    function dfs (path, used) {
        if (path.length >= nums.length) res.push([...path])
        for (let i = 0; i < nums.length; i++) {
            if (used[i]) continue
            used[i] = true
            path.push(nums[i])
            dfs(path, used)
            path.pop()
            used[i] = false
        }
    }
    dfs([], new Array(nums.length).fill(false))
    return res
}