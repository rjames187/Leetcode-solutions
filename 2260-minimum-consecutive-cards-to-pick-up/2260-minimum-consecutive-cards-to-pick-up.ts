function minimumCardPickup(cards: number[]): number {
    const seen = new Map()
    let min = Infinity
    for (let i = 0; i < cards.length; i++) {
        const card = cards[i]
        if (seen.has(card)) {
            min = Math.min(min, i + 1 - seen.get(card))
        }
        seen.set(card, i)
    }
    return min === Infinity ? -1 : min
}