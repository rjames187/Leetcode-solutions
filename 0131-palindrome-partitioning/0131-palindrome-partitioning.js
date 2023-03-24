/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    let res = []
    let part = []
    
    var dfs = function(startIndex) {
        if (startIndex >= s.length) {
            res.push([...part])
            return
        }
        
        for (let end = startIndex; end < s.length; end++) {
            const slice = s.slice(startIndex, end + 1)
            if (!isPalindrome(slice)) continue
            part.push(slice)
            dfs(end + 1)
            part.pop()
        }
    }
    
    dfs(0)
    return res
}

var isPalindrome = function(s) {
    return s === s.split('').reverse().join('')
}