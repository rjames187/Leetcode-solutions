/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
function normalize(str) {
        return str.split("").sort().join("")
}

var isAnagram = function(s, t) {
    return normalize(s) === normalize(t)
};

// time O(N log N)