function lengthOfLongestSubstring(s: string): number {
    let longest = 0, left = 0
    const window = new Map()
    for (let right = 0; right < s.length; right++) {
        const count = window.get(s[right]) || 0
        window.set(s[right], count + 1)
        while (window.get(s[right]) > 1) {
            window.set(s[left], window.get(s[left]) - 1)
            left++
        }
        longest = Math.max(longest, right + 1 - left)
    }
    return longest
}