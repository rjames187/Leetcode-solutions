/**
 * @param {string} s
 * @return {boolean}
 */

function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

function Stack() {
    this.size = 0
    this.top = null
    this.push = (val) => {
        const newNode = new ListNode(val, this.top)
        this.top = newNode
        this.size++
    }
    this.pop = () => {
        const popped = this.top.val
        this.top = this.top.next
        this.size--
    }
}

var isValid = function(s) {
    const stack = new Stack()
    
    const OPENING_BRACKETS = ['(', '[', '{']
    const CLOSING_BRACKETS = [')', ']', '}']
    
    for (c of s.split("")) {
        if (OPENING_BRACKETS.includes(c)) {
            stack.push(c)
        }
        if (CLOSING_BRACKETS.includes(c)) {
            const correspondingBracket = OPENING_BRACKETS[CLOSING_BRACKETS.indexOf(c)]
            if (stack.top && stack.top.val === correspondingBracket) {
                stack.pop()
            } else {
                return false
            }
        }
    }
    
    return stack.size === 0 ? true : false
}