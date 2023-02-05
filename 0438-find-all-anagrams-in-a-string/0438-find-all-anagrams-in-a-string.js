/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var getHash = function (str, i) {
    const asciiCode = str.charCodeAt(i)
    return asciiCode - 'a'.charCodeAt(0)
}

var isEqual = function (arr1, arr2) {
    return arr1.every((e, i) => arr2[i] === e)
}

var findAnagrams = function(s, p) {
    const res = []
    
    let sMap = new Array(26).fill(0)
    let pMap = new Array(26).fill(0)
    
    // first iteration
    for (let i = 0; i < p.length; i++) {
        sMap[getHash(s, i)]++
        pMap[getHash(p, i)]++
    }
    
    if (isEqual(sMap, pMap)) res.push(0)
    
    console.log(sMap.join(''), pMap.join(''))
    // rest of the iterations
    let left = 1
    
    for (let right = p.length; right < s.length; right++) {
        sMap[getHash(s, left - 1)]--
        sMap[getHash(s, right)]++
        if (isEqual(sMap, pMap)) res.push(left)
        left++
    }
    
    return res
}