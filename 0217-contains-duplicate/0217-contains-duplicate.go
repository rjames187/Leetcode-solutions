func containsDuplicate(nums []int) bool {
    m := make(map[int]bool)
    
    for i := 0; i < len(nums); i++ {
        if m[nums[i]] == true {
            return true
        } else {
            m[nums[i]] = true
        }
    }
    
    return false
}