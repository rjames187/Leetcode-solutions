var findEmpty = function(board) {
    for (const r of [0, 1]) {
        for (const c of [0, 1, 2]) {
            if (board[r][c] === 0) return [r, c]
        }
    }
    throw("no empty space on board error")
}

var nextBoards = function(board) {
    const deserialized = JSON.parse(board)
    const [r, c] = findEmpty(deserialized)
    const DELTA_R = [0, 1, 0, -1]
    const DELTA_C = [-1, 0, 1, 0]
    const res = []
    for (const i of [0, 1, 2, 3]) {
        const newR = r + DELTA_R[i]
        if (newR > 1 || newR < 0) continue
        const newC = c + DELTA_C[i]
        if (newC > 2 || newC < 0) continue
        const copyBoard = [[...deserialized[0]], [...deserialized[1]]]
        copyBoard[r][c] = copyBoard[newR][newC]
        copyBoard[newR][newC] = 0
        res.push(JSON.stringify(copyBoard))
    }
    return res
}

/**
 * @param {number[][]} board
 * @return {number}
 */
var slidingPuzzle = function(board) {
    const target = JSON.stringify([[1, 2, 3], [4, 5, 0]])
    const start = JSON.stringify(board)
    if (start === target) return 0
    const visited = new Map()
    visited.set(start, 0)
    const queue = [start]
    while (queue.length) {
        const node = queue.shift()
        for (const newBoard of nextBoards(node)) {
            if (visited.has(newBoard)) continue
            queue.push(newBoard)
            visited.set(newBoard, visited.get(node) + 1)
            if (newBoard === target) return visited.get(newBoard)
        }
    }
    return -1
}