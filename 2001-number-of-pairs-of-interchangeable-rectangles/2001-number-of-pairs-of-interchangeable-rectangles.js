/**
 * @param {number[][]} rectangles
 * @return {number}
 */
var interchangeableRectangles = function(rectangles) {
    const ratioHash = new Map()
    let pairsCount = 0
    
    for (let rectangle of rectangles) {
        const ratio = rectangle[0] / rectangle[1]
        let ratioCount = ratioHash.get(ratio) || 0
        pairsCount += ratioCount
        ratioCount++
        ratioHash.set(ratio, ratioCount)
    }
    
    return pairsCount
}