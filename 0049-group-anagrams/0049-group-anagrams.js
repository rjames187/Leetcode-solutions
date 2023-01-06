/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var addToMap = (indexMap, normWord, originalWord) => {
    if (indexMap.has(normWord)) {
        const curVal = indexMap.get(normWord)
        indexMap.set(normWord, curVal.concat([originalWord]))
    } else {
        indexMap.set(normWord, [originalWord])
    }
}

var groupAnagrams = function(strs) {
    let indexMap = new Map()
    
    for (let i = 0; i < strs.length; i++) {
        let originalWord = strs[i]
        let normWord = originalWord.split('')
        normWord.sort()
        normWord = normWord.join('')
        addToMap(indexMap, normWord, originalWord)
    }
    
    return Array.from(indexMap.values())
};