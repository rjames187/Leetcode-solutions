var increment = function(combo, i) {
    const digits = combo.split('')
    if (digits[i] === '9') digits[i] = '0'
    else digits[i] = String(Number(digits[i]) + 1)
    return digits.join('')
}

var decrement = function(combo, i) {
    const digits = combo.split('')
    if (digits[i] === '0') digits[i] = '9'
    else digits[i] = String(Number(digits[i]) - 1)
    return digits.join('')
}

/**
 * @param {string[]} deadends
 * @param {string} target
 * @return {number}
 */
var openLock = function(deadends, target) {
    deadends = new Set([...deadends])
    if (deadends.has('0000')) return -1
    if (target === '0000') return 0
    const queue = ['0000']
    const steps = new Map()
    steps.set('0000', 0)
    while (queue.length) {
        const combo = queue.shift()
        const curSteps = steps.get(combo)
        for (let i = 0; i < 4; i++) {
            let newCombo = increment(combo, i)
            if (!deadends.has(newCombo) && !steps.has(newCombo)) queue.push(newCombo)
            steps.set(newCombo, curSteps + 1)
            if (target === newCombo) return steps.get(newCombo)
            newCombo = decrement(combo, i)
            if (!deadends.has(newCombo) && !steps.has(newCombo)) queue.push(newCombo)
            steps.set(newCombo, curSteps + 1)
            if (target === newCombo) return steps.get(newCombo)
        }
    }
    return -1
}