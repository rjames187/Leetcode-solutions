var isValidNode = function(image, sr, sc) {
    if (sr < 0 || sr >= image.length) return false
    if (sc < 0 || sc >= image[0].length) return false
    return true
}

var getNeighbors = function(image, sr, sc) {
    const DELTA_ROW = [0, 1, 0, -1]
    const DELTA_COL = [-1, 0, 1, 0]
    const res = []
    const neighbors = new Array(4)
    for (let i = 0; i < 4; i++) {
        const row = sr + DELTA_ROW[i]
        const col = sc + DELTA_COL[i]
        if (isValidNode(image, row, col)) res.push([row, col])
    }
    return res
}

/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, color) {
    var dfs = function(row, col, origColor) {
        if (image[row][col] === color) return
        if (image[row][col] !== origColor) return
        image[row][col] = color
        for (const neighbor of getNeighbors(image, row, col)) {
            const [nRow, nCol] = neighbor
            dfs(nRow, nCol, origColor)
        }
    }
    const origColor = image[sr][sc]
    dfs(sr, sc, origColor)
    return image
}