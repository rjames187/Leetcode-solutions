/**
 * @param {string} digits
 * @return {string[]}
 */
const letters = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

var letterCombinations = function(digits) {
    if (!digits.length) return []
    
    let res = []
    dfs(0, digits, [], res)
    return res
}

var dfs = function(startIndex, digits, path, res) {
    if (startIndex === digits.length) {
        res.push(path.join(''))
        return
    }
    
    const curDigit = digits.charAt(startIndex)
    for (let letter of letters[curDigit]) {
        path.push(letter)
        dfs(startIndex + 1, digits, path, res)
        path.pop()
    }
}