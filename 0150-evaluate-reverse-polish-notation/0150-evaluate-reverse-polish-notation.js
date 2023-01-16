/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    const stack = []
    const OPERATORS = new Set(['+', '-', '*', '/'])
    
    for (token of tokens) {
        if (OPERATORS.has(token)) {
            const b = Number(stack.pop())
            const a = Number(stack.pop())
            let res = null
            switch(token) {
                case '+':
                    res = a + b
                    break
                case '-':
                    res = a - b
                    break
                case '*':
                    res = a * b
                    break
                case '/':
                    res = Math.trunc(a / b)
                    break
            }
            stack.push(res)
        }
        else {
            stack.push(token)
        }
    }
    
    return stack[0]
};