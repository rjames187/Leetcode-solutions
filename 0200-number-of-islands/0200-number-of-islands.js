/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    function validNode(r, c) {
        if (r < 0 || r >= grid.length) return false
        if (c < 0 || c >= grid[0].length) return false
        if (grid[r][c] === '0') return false
        return true
    }
    const DELTA_ROW = [0, 1, 0, -1]
    const DELTA_COL = [-1, 0, 1, 0]
    function dfs(r, c) {
        for (let i = 0; i < 4; i++) {
            const [nr, nc] = [r + DELTA_ROW[i], c + DELTA_COL[i]]
            if (!validNode(nr, nc)) continue
            grid[nr][nc] = '0'
            dfs(nr, nc)
        }
    }
    let islands = 0
    for (let r = 0; r < grid.length; r++) {
        for (let c = 0; c < grid[0].length; c++) {
            if (grid[r][c] === '0') continue
            dfs(r, c)
            islands++
        }
    }
    return islands
}