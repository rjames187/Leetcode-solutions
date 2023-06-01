
var TimeLimitedCache = function() {
    this.cache = new Map()
}

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const exists = this.cache.has(key)
    if (exists) clearTimeout(this.cache.get(key)[1])
    const ref = setTimeout(() => {
        this.cache.delete(key)
    }, duration)
    this.cache.set(key, [value, ref])
    return exists
}

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (this.cache.has(key)) return this.cache.get(key)[0]
    return -1
}

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    const keys = Array.from(this.cache.keys())
    return keys.length
}

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */