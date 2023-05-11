/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    function util(functions, x) {
        const func = functions.shift()
        if (functions.length === 0) return func(x)
        return func(util(functions, x))
    }
	return function(x) {
        if (functions.length === 0) return x
        return util(functions, x)
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */