function subarraySum(nums: number[], k: number): number {
    const prefixSums = new Map()
    prefixSums.set(0, 1)
    let curSum = 0
    let count = 0
    for (let i = 0; i < nums.length; i++) {
        curSum += nums[i]
        const prefixSum = curSum - k
        if (prefixSums.has(prefixSum)) {
            count += prefixSums.get(prefixSum)
        }
        prefixSums.set(curSum, (prefixSums.get(curSum) || 0) + 1)
    }
    return count
}