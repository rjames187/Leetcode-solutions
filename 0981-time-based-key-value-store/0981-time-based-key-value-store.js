
var TimeMap = function() {
    this.table = new Map()
}

/** 
 * @param {string} key 
 * @param {string} value 
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function(key, value, timestamp) {
    const vals = this.table.get(key) || []
    vals.push([value, timestamp])
    this.table.set(key, vals)
}

var searchByTimeStamp = function(vals, time) {
    if (vals.length < 1 || time < vals[0][1]) return ""
    
    let left = 0
    let right = vals.length - 1
    let boundary = left
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        
        if (vals[mid][1] === time) {
            return vals[mid][0]
        }
        if (vals[mid][1] < time) {
            boundary = mid
            left = mid + 1
        }
        else right = mid - 1
    }
    
    return vals[boundary][0]
}

/** 
 * @param {string} key 
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function(key, timestamp) {
    const vals = this.table.get(key) || []
    return searchByTimeStamp(vals, timestamp)
}

/** 
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */