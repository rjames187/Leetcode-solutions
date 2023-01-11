/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidNum = (uniqueNums, curNum) => {
    if (curNum === '.') {
        return true
    }
    if (uniqueNums.has(curNum)) {
        return false
    }
    uniqueNums.add(curNum)
    return true
}

var areValidRowCols = (board, type) => {
    for (let i = 0; i < 9; i++) {
        let uniqueNums = new Set()
        for (let j = 0; j < 9; j++) {
            const curNum = type === "row" ? board[i][j] : board[j][i]
            if (!isValidNum(uniqueNums, curNum)) {
                console.log(`invalid row/col at ${i} ${j}`)
                return false
            }
        }
    }
    console.log('valid row/col')
    return true
}

var isValidSubBox = (x, y, board) => {
    let uniqueNums = new Set()
    
    for (let i = x; i < x + 3; i++) {
        for (let j = y; j < y + 3; j++) {
            const curNum = board[i][j]
            
            if (!isValidNum(uniqueNums, curNum)) {
                return false
            }
        }
    }
    
    return true
}

var areValidSubBoxes = (board) => {
    for (let i = 0; i <= 6; i += 3) {
        for (let j = 0; j <= 6; j += 3) {
            if (!isValidSubBox(i, j, board)) {
                console.log(`invalid sub box at ${i} ${j}`)
                return false
            }
        }
    }
    return true
}


var isValidSudoku = function(board) {
    let valid = areValidRowCols(board, "row") && areValidRowCols(board, "col")
    return valid && areValidSubBoxes(board)
};