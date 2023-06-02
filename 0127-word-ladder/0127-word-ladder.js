var getNewWord = function(word, i, j) {
    const letters = word.split('')
    letters[i] = String.fromCharCode(j)
    return letters.join('')
}

/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
    const queue = [beginWord]
    const dict = new Set([...wordList])
    const words = new Map()
    words.set(beginWord, 1)
    while (queue.length) {
        const word = queue.shift()
        for (let i = 0; i < word.length; i++) {
            for (let j = 97; j <= 122; j++) {
                const newWord = getNewWord(word, i, j)
                if (!dict.has(newWord) || words.has(newWord)) continue
                queue.push(newWord)
                words.set(newWord, words.get(word) + 1)
                if (newWord === endWord) return words.get(newWord)
            }
        }
    }
    return 0
}