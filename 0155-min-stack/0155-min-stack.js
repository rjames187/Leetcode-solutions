var Node = function(val, next) {
    this.val = val
    this.next = next
    this.minVal = Math.POSITIVE_INFINITY
}


var MinStack = function() {
    this.head = null
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    const newNode = new Node(val, this.head)
    newNode.minVal = this.head ? Math.min(this.head.minVal, newNode.val) : newNode.val
    this.head = newNode
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.head = this.head.next
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.head.val
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.head.minVal
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */